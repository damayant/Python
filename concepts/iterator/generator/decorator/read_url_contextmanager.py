import urllib.request

url = "https://www.example.com/some_file.txt"

try:
    with urllib.request.urlopen(url) as response:
        # Read the entire content of the file
        file_content = response.read().decode('utf-8')
        print(file_content)

        # Or, read line by line
        # for line in response:
        #     print(line.decode('utf-8').strip())

except urllib.error.URLError as e:
    print(f"Error accessing URL: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")