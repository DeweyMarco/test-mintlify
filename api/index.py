"""
Quotes API — pure stdlib, no dependencies required.
Run with: python3 api/index.py
"""

import json
import random
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

QUOTES = [
    {"id": "1", "text": "The only way to do great work is to love what you do.", "author": "Steve Jobs", "category": "motivation"},
    {"id": "2", "text": "In the middle of every difficulty lies opportunity.", "author": "Albert Einstein", "category": "motivation"},
    {"id": "3", "text": "It does not matter how slowly you go as long as you do not stop.", "author": "Confucius", "category": "motivation"},
    {"id": "4", "text": "The unexamined life is not worth living.", "author": "Socrates", "category": "philosophy"},
    {"id": "5", "text": "I think, therefore I am.", "author": "René Descartes", "category": "philosophy"},
    {"id": "6", "text": "The only true wisdom is in knowing you know nothing.", "author": "Socrates", "category": "wisdom"},
    {"id": "7", "text": "Yesterday I was clever, so I wanted to change the world. Today I am wise, so I am changing myself.", "author": "Rumi", "category": "wisdom"},
    {"id": "8", "text": "In three words I can sum up everything I've learned about life: it goes on.", "author": "Robert Frost", "category": "wisdom"},
    {"id": "11", "text": "The computer was born to solve problems that did not exist before.", "author": "Bill Gates", "category": "technology"},
    {"id": "12", "text": "Any sufficiently advanced technology is indistinguishable from magic.", "author": "Arthur C. Clarke", "category": "technology"},
    {"id": "13", "text": "The advance of technology is based on making it fit in so that you don't really even notice it.", "author": "Bill Gates", "category": "technology"},
    {"id": "14", "text": "Simplicity is the ultimate sophistication.", "author": "Leonardo da Vinci", "category": "wisdom"},
    {"id": "16", "text": "Why should I go to his funeral, he isn't coming to mine.", "author": "Marco Dewey", "category": "marco original"},
]

VALID_CATEGORIES = sorted(set(q["category"] for q in QUOTES))
QUOTES_BY_ID = {q["id"]: q for q in QUOTES}
PORT = 3000


class Handler(BaseHTTPRequestHandler):
    def log_message(self, format, *args):
        print(f"  {self.command} {self.path} -> {args[1]}")

    def send_json(self, status, data):
        body = json.dumps(data, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path.rstrip("/")
        params = parse_qs(parsed.query)

        # GET /categories
        if path == "/categories":
            self.send_json(200, {"categories": VALID_CATEGORIES})
            return

        # GET /quotes/random
        if path == "/quotes/random":
            category = params.get("category", [None])[0]
            if category and category not in VALID_CATEGORIES:
                self.send_json(400, {
                    "error": "invalid_category",
                    "message": f"Category '{category}' does not exist. Valid categories: {', '.join(VALID_CATEGORIES)}",
                })
                return
            pool = [q for q in QUOTES if q["category"] == category] if category else QUOTES
            self.send_json(200, random.choice(pool))
            return

        # GET /quotes
        if path == "/quotes":
            category = params.get("category", [None])[0]
            limit = params.get("limit", [None])[0]

            if category and category not in VALID_CATEGORIES:
                self.send_json(400, {
                    "error": "invalid_category",
                    "message": f"Category '{category}' does not exist. Valid categories: {', '.join(VALID_CATEGORIES)}",
                })
                return

            results = [q for q in QUOTES if q["category"] == category] if category else list(QUOTES)

            if limit is not None:
                try:
                    n = int(limit)
                    if n < 1:
                        raise ValueError
                    results = results[:n]
                except ValueError:
                    self.send_json(400, {"error": "invalid_limit", "message": "limit must be a positive integer"})
                    return

            self.send_json(200, {"quotes": results, "total": len(results)})
            return

        # GET /quotes/{id}
        if path.startswith("/quotes/"):
            quote_id = path[len("/quotes/"):]
            quote = QUOTES_BY_ID.get(quote_id)
            if not quote:
                self.send_json(404, {"error": "not_found", "message": f"No quote found with id '{quote_id}'"})
                return
            self.send_json(200, quote)
            return

        self.send_json(404, {"error": "not_found", "message": f"Route '{path}' not found"})


if __name__ == "__main__":
    server = HTTPServer(("localhost", PORT), Handler)
    print(f"Quotes API running on http://localhost:{PORT}")
    server.serve_forever()
