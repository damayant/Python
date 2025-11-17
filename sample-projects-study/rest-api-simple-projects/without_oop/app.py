"""Simple REST API without OOP (procedural approach).

This demonstrates a functional programming approach to building APIs.
Note: For production, OOP approach (see with_oop/app.py) is recommended.
"""

import logging
from typing import Dict, List, Optional, Tuple

from flask import Flask, request, jsonify

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# In-memory data storage
books_db: List[Dict] = []
next_book_id: int = 1


def validate_book_data(data: Dict) -> Tuple[bool, Optional[str]]:
    """Validate book data.

    Args:
        data: Book data dictionary

    Returns:
        Tuple of (is_valid, error_message)
    """
    if not isinstance(data, dict):
        return False, "Data must be a dictionary"

    required_fields = ["title", "author"]
    for field in required_fields:
        if field not in data or not isinstance(data.get(field), str):
            return False, f"Missing or invalid required field: {field}"

    if not data["title"].strip():
        return False, "Title cannot be empty"

    if not data["author"].strip():
        return False, "Author cannot be empty"

    return True, None


def find_book_by_id(book_id: int) -> Optional[Dict]:
    """Find book by ID in database.

    Args:
        book_id: Book ID to search

    Returns:
        Book dictionary or None if not found
    """
    for book in books_db:
        if book["id"] == book_id:
            return book
    return None


def create_book(title: str, author: str, year: Optional[int] = None) -> Dict:
    """Create a new book entry.

    Args:
        title: Book title
        author: Book author
        year: Publication year (optional)

    Returns:
        Created book dictionary
    """
    global next_book_id

    book = {
        "id": next_book_id,
        "title": title.strip(),
        "author": author.strip(),
        "year": year,
    }

    books_db.append(book)
    next_book_id += 1
    logger.info(f"Created book: {book}")
    return book


@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint.

    Returns:
        JSON status response
    """
    logger.debug("Health check requested")
    return jsonify({"status": "healthy"}), 200


@app.route("/books", methods=["GET"])
def list_books():
    """List all books.

    Returns:
        JSON array of books
    """
    logger.info(f"Listing {len(books_db)} books")
    return jsonify({"books": books_db}), 200


@app.route("/books", methods=["POST"])
def add_book():
    """Add a new book.

    Request JSON:
        - title (required): Book title
        - author (required): Book author
        - year (optional): Publication year

    Returns:
        JSON with created book or error message
    """
    if not request.is_json:
        error_msg = "Request must be JSON"
        logger.warning(error_msg)
        return jsonify({"error": error_msg}), 400

    data = request.get_json()
    is_valid, error_msg = validate_book_data(data)

    if not is_valid:
        logger.warning(f"Invalid book data: {error_msg}")
        return jsonify({"error": error_msg}), 400

    try:
        book = create_book(
            title=data["title"],
            author=data["author"],
            year=data.get("year"),
        )
        return jsonify(book), 201

    except Exception as e:
        error_msg = f"Failed to create book: {str(e)}"
        logger.error(error_msg)
        return jsonify({"error": error_msg}), 500


@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id: int):
    """Get a specific book by ID.

    Args:
        book_id: Book ID

    Returns:
        JSON with book data or error message
    """
    logger.info(f"Retrieving book with ID: {book_id}")
    book = find_book_by_id(book_id)

    if not book:
        error_msg = f"Book with ID {book_id} not found"
        logger.warning(error_msg)
        return jsonify({"error": error_msg}), 404

    return jsonify(book), 200


@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id: int):
    """Update a book.

    Args:
        book_id: Book ID

    Returns:
        JSON with updated book or error message
    """
    if not request.is_json:
        error_msg = "Request must be JSON"
        logger.warning(error_msg)
        return jsonify({"error": error_msg}), 400

    book = find_book_by_id(book_id)
    if not book:
        error_msg = f"Book with ID {book_id} not found"
        logger.warning(error_msg)
        return jsonify({"error": error_msg}), 404

    data = request.get_json()

    # Update only provided fields
    if "title" in data:
        if not isinstance(data["title"], str) or not data["title"].strip():
            return jsonify({"error": "Title must be non-empty string"}), 400
        book["title"] = data["title"].strip()

    if "author" in data:
        if not isinstance(data["author"], str) or not data["author"].strip():
            return jsonify({"error": "Author must be non-empty string"}), 400
        book["author"] = data["author"].strip()

    if "year" in data:
        book["year"] = data["year"]

    logger.info(f"Updated book with ID: {book_id}")
    return jsonify(book), 200


@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id: int):
    """Delete a book.

    Args:
        book_id: Book ID

    Returns:
        JSON success message or error
    """
    book = find_book_by_id(book_id)
    if not book:
        error_msg = f"Book with ID {book_id} not found"
        logger.warning(error_msg)
        return jsonify({"error": error_msg}), 404

    books_db.remove(book)
    logger.info(f"Deleted book with ID: {book_id}")
    return jsonify({"message": f"Book {book_id} deleted"}), 200


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors.

    Args:
        error: Error object

    Returns:
        JSON error response
    """
    logger.warning(f"404 Not Found: {request.path}")
    return jsonify({"error": "Endpoint not found"}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors.

    Args:
        error: Error object

    Returns:
        JSON error response
    """
    logger.error(f"500 Internal Server Error: {str(error)}")
    return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    logger.info("Starting REST API (without OOP)")
    app.run(debug=True, port=5000)

