import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from queue import Queue
from urllib.parse import urlparse

# Define a global queue to store jobs
job_queue = Queue()

# Allowed job types
VALID_JOBS = {"process_game", "delete_events", "scrape_events"}

class JobHandler(BaseHTTPRequestHandler):
    def _set_response(self, status_code=200):
        self.send_response(status_code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

    def do_POST(self):
        # Parse URL path
        parsed_path = urlparse(self.path)
        if parsed_path.path != "/submit_job":
            self._set_response(404)
            self.wfile.write(json.dumps({"error": "Endpoint not found"}).encode())
            return

        # Read and parse request body
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)

        try:
            data = json.loads(body)
        except json.JSONDecodeError:
            self._set_response(400)
            self.wfile.write(json.dumps({"error": "Invalid JSON format"}).encode())
            return

        # Validate job name presence
        job_name = data.get("job_name")
        if not job_name:
            self._set_response(400)
            self.wfile.write(json.dumps({"error": "Missing required field: job_name"}).encode())
            return

        # Validate allowed jobs
        if job_name not in VALID_JOBS:
            self._set_response(422)  # 422 Unprocessable Entity
            self.wfile.write(json.dumps({
                "error": f"Invalid job name '{job_name}'. Must be one of {list(VALID_JOBS)}"
            }).encode())
            return

        # Submit job to queue
        job_queue.put(job_name)
        self._set_response(200)
        self.wfile.write(json.dumps({
            "message": f"Job '{job_name}' submitted successfully",
            "queue_size": job_queue.qsize()
        }).encode())

    # Suppress noisy default logging
    def log_message(self, format, *args):
        return


def run(server_class=HTTPServer, handler_class=JobHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"🚀 Server running on http://localhost:{port}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down server...")
    finally:
        httpd.server_close()


if __name__ == "__main__":
    run()
