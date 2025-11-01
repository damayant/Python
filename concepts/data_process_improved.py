import requests
import logging
import json
import re # Used for simple text analysis

# 1. Setup Logging (Essential for robust applications)
# Logs all INFO and ERROR messages to a file named 'data_retrieval.log'
logging.basicConfig(
    filename="data_retrieval.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

def get_data_and_extract_metadata(base_url, timeout_limit=10, chunk_limit=1024, stream=False):
    """
    Fetches data from an endpoint, handles JSON or streams large files,
    and extracts basic metadata efficiently.
    """
    # 2. Create a Session for connection reuse and efficiency
    session = requests.Session()
    
    # Initialize a dictionary to store all useful findings
    extracted_metadata = {'url': base_url, 'data_type': 'Unknown', 'size_bytes': 0}

    try:
        # 3. Use Context Manager for the request to ensure connection cleanup
        with session.get(url=base_url, timeout=timeout_limit, stream=stream) as response:
            # 4. Check for HTTP errors (4xx or 5xx)
            response.raise_for_status()

            # 5. Check Content Type and Headers
            content_type = response.headers.get('Content-Type', '')
            extracted_metadata['data_type'] = content_type
            
            # --- Path A: Streaming for Large Data ---
            if stream and 'text' in content_type:
                output_filename = "downloaded_streamed_data.txt"
                total_bytes_processed = 0
                
                logging.info(f"Starting stream for {base_url} to {output_filename}")
                
                # Write the streamed bytes directly to a local file
                with open(output_filename, 'wb') as f:
                    for chunk_bytes in response.iter_content(chunk_size=chunk_limit):
                        if chunk_bytes:
                            f.write(chunk_bytes) # Write bytes directly (low memory usage)
                            total_bytes_processed += len(chunk_bytes)
                            
                extracted_metadata['size_bytes'] = total_bytes_processed
                extracted_metadata['local_path'] = output_filename
                
                # Metadata Extraction: Analyze the first 1KB *after* download for a clean process
                try:
                    with open(output_filename, 'r', encoding='utf-8') as f_read:
                        first_k = f_read.read(1024)
                        # Example: Count unique words in the first 1KB of the file
                        words = re.findall(r'\b\w+\b', first_k.lower())
                        extracted_metadata['unique_words_in_header'] = len(set(words))
                except Exception:
                    logging.warning("Failed to read file header for metadata.")
                
                # We return the metadata map, which includes the file's local path.
                return extracted_metadata
                
            # --- Path B: JSON Data ---
            elif 'application/json' in content_type:
                data = response.json()
                extracted_metadata['size_bytes'] = len(response.content)
                
                # Metadata Extraction for JSON: Count records and sample keys
                if isinstance(data, list):
                    extracted_metadata['record_count'] = len(data)
                    if data and isinstance(data[0], dict):
                         extracted_metadata['sample_keys'] = list(data[0].keys())
                elif isinstance(data, dict):
                    extracted_metadata['record_count'] = 1
                    extracted_metadata['sample_keys'] = list(data.keys())

                extracted_metadata['data'] = data # Return the parsed data
                return extracted_metadata
                
            # --- Path C: Small Text Data (Non-JSON) ---
            else:
                text_content = response.text
                extracted_metadata['size_bytes'] = len(response.content)
                extracted_metadata['data'] = text_content
                
                # Simple text metadata: character count
                extracted_metadata['char_count'] = len(text_content)
                return extracted_metadata

    except requests.RequestException as e:
        # Catch all request-related errors (timeout, connection, 4xx/5xx from raise_for_status)
        logging.error(f'Request failed for {base_url}:{e}')
        return None
        
    # 6. Guaranteed Cleanup
    finally:
        # This always runs, ensuring the Session connection is closed safely.
        session.close()

# --- Usage Examples ---
BASE_URL_JSON = 'https://jsonplaceholder.typicode.com/posts/1'
BASE_URL_TEXT_FILE = 'https://raw.githubusercontent.com/damayant/Python/master/api/sample.txt'

print("\n--- JSON API Processing ---")
json_result = get_data_and_extract_metadata(BASE_URL_JSON)
if json_result:
    print(f"Metadata Extracted (JSON): {json.dumps({k: v for k, v in json_result.items() if k != 'data'}, indent=2)}")
    print(f"Data Sample (Title): {json_result['data'].get('title', 'N/A')}")

print("\n--- Streaming and File Writing ---")
stream_result = get_data_and_extract_metadata(BASE_URL_TEXT_FILE, stream=True)
if stream_result:
    print(f"Metadata Extracted (Streamed File): {json.dumps(stream_result, indent=2)}")
    print(f"File saved locally to: {stream_result.get('local_path')}")