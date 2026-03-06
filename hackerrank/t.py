from playwright.sync_api import sync_playwright

OUTPUT = "./pdf"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.hellointerview.com/learn/system-design/")
    page.pdf(path=OUTPUT)
    browser.close()

print("DONE")
