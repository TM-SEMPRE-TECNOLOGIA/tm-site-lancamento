import http.server
import os
import sys

class RangeHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def send_head(self):
        path = self.translate_path(self.path)
        if os.path.isdir(path):
            return super().send_head()

        try:
            f = open(path, 'rb')
        except OSError:
            self.send_error(404, "File not found")
            return None

        fs = os.fstat(f.fileno())
        size = fs.st_size

        range_header = self.headers.get('Range')
        if not range_header or not range_header.startswith('bytes='):
            self.send_response(200)
            self.send_header("Content-type", self.guess_type(path))
            self.send_header("Content-Length", str(size))
            self.send_header("Accept-Ranges", "bytes")
            self.end_headers()
            return f

        # Parse range header
        try:
            range_val = range_header.strip().split('=')[1]
            start_str, end_str = range_val.split('-')
            start = int(start_str) if start_str else 0
            end = int(end_str) if end_str else size - 1
            if start >= size or end >= size or start > end:
                self.send_error(416, "Requested Range Not Satisfiable")
                f.close()
                return None
        except Exception:
            self.send_error(400, "Bad Request")
            f.close()
            return None

        content_length = end - start + 1
        self.send_response(206)
        self.send_header("Content-type", self.guess_type(path))
        self.send_header("Content-Range", f"bytes {start}-{end}/{size}")
        self.send_header("Content-Length", str(content_length))
        self.send_header("Accept-Ranges", "bytes")
        self.end_headers()

        f.seek(start)
        return RangeFileWrapper(f, content_length)

class RangeFileWrapper:
    def __init__(self, file_obj, length):
        self.file_obj = file_obj
        self.bytes_remaining = length

    def read(self, size=-1):
        if self.bytes_remaining <= 0:
            return b""
        if size < 0 or size > self.bytes_remaining:
            size = self.bytes_remaining
        data = self.file_obj.read(size)
        self.bytes_remaining -= len(data)
        return data

    def close(self):
        self.file_obj.close()

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    server = http.server.HTTPServer(('127.0.0.1', port), RangeHTTPRequestHandler)
    print(f"Range-supporting server running on http://127.0.0.1:{port}")
    server.serve_forever()
