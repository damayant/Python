import os
import time
import logging
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from playwright.sync_api import sync_playwright

BASE_URL = "https://www.hellointerview.com/learn/system-design/"
LOGIN_URL = "https://www.hellointerview.com/login"
OUTPUT_DIR = "./pdf"
EMAIL = "damayantishrobon@gmail.com"

# Setup logging for debugging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

os.makedirs(OUTPUT_DIR, exist_ok=True)


def login_with_email(page, email):
    """
    Login to hellointerview.com using email and verification code.
    Auto-detects when authentication is complete.
    """
    try:
        logging.info(f"Navigating to login page: {LOGIN_URL}")
        page.goto(LOGIN_URL, timeout=60000)
        
        # Wait for and click "Continue With Email" button
        logging.info("Waiting for 'Continue With Email' button...")
        continue_email_button = page.locator("button:has-text('Continue With Email'), button:has-text('Continue with Email')").first
        if continue_email_button.is_visible():
            logging.info("Clicking 'Continue With Email' button...")
            continue_email_button.click()
            time.sleep(1)  # Wait for form to appear
        else:
            logging.warning("'Continue With Email' button not found, proceeding to email input...")
        
        # Wait for email input field to be visible
        logging.info("Waiting for email input field...")
        page.wait_for_selector("input[type='email'], input[placeholder*='email' i]", timeout=100000)
        
        # Fill in email
        logging.info(f"Entering email: {email}")
        email_input = page.locator("input[type='email'], input[placeholder*='email' i]").first
        email_input.fill(email)
        
        # Click submit/continue button
        logging.info("Looking for submit button...")
        submit_button = page.locator("button:has-text('Continue'), button:has-text('Send'), button:has-text('Next')").first
        if submit_button.is_visible():
            submit_button.click()
            logging.info("Clicked submit button, waiting for verification...")
        else:
            logging.warning("Submit button not found, trying to press Enter...")
            page.press("input[type='email']", "Enter")
        
        # Wait for verification code page to load
        time.sleep(100000)
        
        logging.info(f"\n{'='*60}")
        logging.info(f"Verification code has been sent to {email}")
        logging.info(f"Please check your email and verify in the browser")
        logging.info(f"Waiting for automatic verification...")
        logging.info(f"{'='*60}\n")
        
        # Wait for authentication to complete by checking if we're no longer on login page
        # Check every 2 seconds for up to 10 minutes
        max_wait_time = 600  # 10 minutes
        check_interval = 2
        elapsed_time = 0
        
        while elapsed_time < max_wait_time:
            current_url = page.url
            if "login" not in current_url.lower():
                logging.info(f"\n✓ Login successful! Current URL: {current_url}")
                time.sleep(2)  # Give page time to fully load after auth
                return True
            
            # Show progress every 30 seconds instead of every 2 seconds
            if elapsed_time % 30 == 0:
                remaining_time = max_wait_time - elapsed_time
                logging.info(f"Waiting for authentication... ({elapsed_time}s elapsed, {remaining_time}s remaining)")
            time.sleep(check_interval)
            elapsed_time += check_interval
        
        # If we timeout waiting for authentication
        logging.error(f"Timeout waiting for authentication after {max_wait_time} seconds")
        return False
            
    except Exception as e:
        logging.error(f"Login failed: {type(e).__name__}: {e}")
        return False


def get_all_links(page):
    """
    Crawl the system-design section and extract lesson URLs using authenticated browser
    """
    # Navigate to the base URL using the authenticated browser
    logging.info(f"Scraping links from {BASE_URL} using authenticated browser...")
    page.goto(BASE_URL, timeout=30000)
    page.wait_for_load_state("domcontentloaded", timeout=100000)
    
    # Get page content
    html_content = page.content()
    soup = BeautifulSoup(html_content, "html.parser")

    links = set()
    for a in soup.find_all("a", href=True):
        href = a["href"]
        full_url = urljoin(BASE_URL, href)

        if full_url.startswith(BASE_URL):
            parsed = urlparse(full_url)
            clean_url = parsed.scheme + "://" + parsed.netloc + parsed.path
            links.add(clean_url)

    return sorted(links)


def save_page_as_pdf(page, url):
    """
    Render page and save as PDF
    """
    slug = url.rstrip("/").split("/")[-1]
    if not slug:  # fallback for root URLs
        slug = "index"
    filename = f"{slug}.pdf"
    filepath = os.path.join(OUTPUT_DIR, filename)

    try:
        logging.info(f"Processing: {url}")
        page.goto(url, timeout=30000)  # 30 second timeout
        logging.info(f"  Loaded, waiting for network to settle...")
        
        # Use a shorter timeout for networkidle and fallback to domcontentloaded
        try:
            page.wait_for_load_state("networkidle", timeout=10000)  # 10 second timeout
        except:
            logging.warning(f"  Network idle timeout, using domcontentloaded instead")
            page.wait_for_load_state("domcontentloaded", timeout=5000)
        
        logging.info(f"  Generating PDF: {filename}")
        page.pdf(
            path=filepath,
            format="A4",
            margin={"top": "20px", "bottom": "20px", "left": "20px", "right": "20px"},
            print_background=True
        )
        
        if os.path.exists(filepath):
            size = os.path.getsize(filepath)
            logging.info(f"  ✓ PDF saved: {filename} ({size} bytes)")
        else:
            logging.error(f"  ✗ PDF file not created for {url}")
            
    except Exception as e:
        logging.error(f"  ✗ Failed to process {url}: {type(e).__name__}: {e}")


def main():
    try:
        with sync_playwright() as p:
            logging.info("Launching Chromium browser...")
            browser = p.chromium.launch(headless=False)  # headless=False to see login flow
            page = browser.new_page()
            
            # Step 1: Login first
            logging.info("="*60)
            logging.info("STEP 1: Logging in to hellointerview.com")
            logging.info("="*60)
            if not login_with_email(page, EMAIL):
                logging.error("Login failed, cannot proceed with crawling.")
                browser.close()
                return
            
            # Step 2: Navigate to the base URL (to ensure we're on the right domain after login)
            logging.info("\n" + "="*60)
            logging.info("STEP 2: Navigating to system design section")
            logging.info("="*60)
            page.goto(BASE_URL, timeout=30000)
            page.wait_for_load_state("domcontentloaded", timeout=10000)
            logging.info(f"✓ Navigated to {BASE_URL}")
            
            # Step 3: Get all links using authenticated browser
            logging.info("\n" + "="*60)
            logging.info("STEP 3: Crawling for lesson links (using authenticated browser)")
            logging.info("="*60)
            urls = get_all_links(page)
            logging.info(f"Found {len(urls)} pages to process")
            
            if not urls:
                logging.warning("No URLs found, exiting.")
                browser.close()
                return

            # Step 4: Generate PDFs
            logging.info("\n" + "="*60)
            logging.info("STEP 4: Generating PDFs from premium content")
            logging.info("="*60)
            
            success_count = 0
            fail_count = 0

            for idx, url in enumerate(urls, 1):
                logging.info(f"\n[{idx}/{len(urls)}] Processing: {url}")
                try:
                    save_page_as_pdf(page, url)
                    success_count += 1
                    time.sleep(1)  # be polite to the server
                except Exception as e:
                    logging.error(f"Unexpected error for {url}: {e}")
                    fail_count += 1

            browser.close()
            logging.info(f"\n{'='*60}")
            logging.info(f"Done! Generated {success_count} PDFs, {fail_count} failed")
            logging.info(f"PDFs saved to: {os.path.abspath(OUTPUT_DIR)}")
            logging.info(f"{'='*60}")
            
    except Exception as e:
        logging.error(f"Fatal error: {type(e).__name__}: {e}", exc_info=True)


if __name__ == "__main__":
    main()
