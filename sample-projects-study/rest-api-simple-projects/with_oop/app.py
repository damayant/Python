"""REST API with OOP (Object-Oriented Programming approach).

This demonstrates a professional OOP approach to building APIs using
service layer pattern, dependency injection, and clean architecture.
"""

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional

from flask import Flask, request, jsonify


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class Book:
    """Book model using dataclass."""

    id: int
    title: str
    author: str
    year: Optional[int] = None

    def to_dict(self) -> Dict:
        """Convert book to dictionary.

        Returns:
            Dictionary representation of book
        """
        return asdict(self)


class ValidationError(Exception):
    """Custom validation error exception."""

    pass


class NotFoundError(Exception):
    """Custom not found error exception."""

    pass


class Repository(ABC):
    """Abstract base class for data repositories."""

    @abstractmethod
    def add(self, book: Book) -> None:
        """Add book to repository.

        Args:
            book: Book instance to add
        """
        pass

    @abstractmethod
    def find_by_id(self, book_id: int) -> Optional[Book]:
        """Find book by ID.

        Args:
            book_id: Book ID to find

        Returns:
            Book instance or None
        """
        pass

    @abstractmethod
    def find_all(self) -> List[Book]:
        """Get all books.

        Returns:
            List of all books
        """
        pass

    @abstractmethod
    def update(self, book: Book) -> None:
        """Update existing book.

        Args:
            book: Updated book instance
        """
        pass

    @abstractmethod
    def delete(self, book_id: int) -> None:
        """Delete book by ID.

        Args:
            book_id: Book ID to delete
        """
        pass


class InMemoryRepository(Repository):
    """In-memory implementation of Repository."""

    def __init__(self):
        """Initialize in-memory repository."""
        self._books: Dict[int, Book] = {}
        self._next_id: int = 1

    def add(self, book: Book) -> None:
        """Add book to repository.

        Args:
            book: Book instance to add
        """
        book.id = self._next_id
        self._books[self._next_id] = book
        self._next_id += 1
        logger.debug(f"Added book: {book}")

    def find_by_id(self, book_id: int) -> Optional[Book]:
        """Find book by ID.

        Args:
            book_id: Book ID to find

        Returns:
            Book instance or None
        """
        return self._books.get(book_id)

    def find_all(self) -> List[Book]:
        """Get all books.

        Returns:
            List of all books
        """
        return list(self._books.values())

    def update(self, book: Book) -> None:
        """Update existing book.

        Args:
            book: Updated book instance

        Raises:
            NotFoundError: If book not found
        """
        if book.id not in self._books:
            raise NotFoundError(f"Book with ID {book.id} not found")
        self._books[book.id] = book
        logger.debug(f"Updated book: {book}")

    def delete(self, book_id: int) -> None:
        """Delete book by ID.

        Args:
            book_id: Book ID to delete

        Raises:
            NotFoundError: If book not found
        """
        if book_id not in self._books:
            raise NotFoundError(f"Book with ID {book_id} not found")
        del self._books[book_id]
        logger.debug(f"Deleted book with ID: {book_id}")


class BookValidator:
    """Validator for book data."""

    @staticmethod
    def validate_create_data(data: Dict) -> None:
        """Validate data for creating book.

        Args:
            data: Data to validate

        Raises:
            ValidationError: If validation fails
        """
        if not isinstance(data, dict):
            raise ValidationError("Data must be a dictionary")

        required_fields = ["title", "author"]
        for field in required_fields:
            if field not in data:
                raise ValidationError(f"Missing required field: {field}")

            if not isinstance(data[field], str):
                raise ValidationError(f"Field '{field}' must be string")

            if not data[field].strip():
                raise ValidationError(f"Field '{field}' cannot be empty")

    @staticmethod
    def validate_update_data(data: Dict) -> None:
        """Validate data for updating book.

        Args:
            data: Data to validate

        Raises:
            ValidationError: If validation fails
        """
        if not isinstance(data, dict):
            raise ValidationError("Data must be a dictionary")

        for field in ["title", "author"]:
            if field in data:
                if not isinstance(data[field], str):
                    raise ValidationError(f"Field '{field}' must be string")
                if not data[field].strip():
                    raise ValidationError(f"Field '{field}' cannot be empty")


class BookService:
    """Service layer for book operations."""

    def __init__(self, repository: Repository, validator: BookValidator):
        """Initialize service.

        Args:
            repository: Book repository instance
            validator: Book validator instance
        """
        self.repository = repository
        self.validator = validator
        self.logger = logging.getLogger(self.__class__.__name__)

    def create_book(self, data: Dict) -> Book:
        """Create a new book.

        Args:
            data: Book data

        Returns:
            Created book instance

        Raises:
            ValidationError: If data is invalid
        """
        self.validator.validate_create_data(data)

        book = Book(
            id=0,  # Will be set by repository
            title=data["title"].strip(),
            author=data["author"].strip(),
            year=data.get("year"),
        )

        self.repository.add(book)
        self.logger.info(f"Created book: {book}")
        return book

    def get_book(self, book_id: int) -> Book:
        """Get book by ID.

        Args:
            book_id: Book ID

        Returns:
            Book instance

        Raises:
            NotFoundError: If book not found
        """
        book = self.repository.find_by_id(book_id)
        if not book:
            raise NotFoundError(f"Book with ID {book_id} not found")
        return book

    def get_all_books(self) -> List[Book]:
        """Get all books.

        Returns:
            List of all books
        """
        books = self.repository.find_all()
        self.logger.info(f"Retrieved {len(books)} books")
        return books

    def update_book(self, book_id: int, data: Dict) -> Book:
        """Update existing book.

        Args:
            book_id: Book ID
            data: Updated book data

        Returns:
            Updated book instance

        Raises:
            ValidationError: If data is invalid
            NotFoundError: If book not found
        """
        self.validator.validate_update_data(data)

        book = self.get_book(book_id)

        # Update fields
        if "title" in data:
            book.title = data["title"].strip()
        if "author" in data:
            book.author = data["author"].strip()
        if "year" in data:
            book.year = data["year"]

        self.repository.update(book)
        self.logger.info(f"Updated book: {book}")
        return book

    def delete_book(self, book_id: int) -> None:
        """Delete book.

        Args:
            book_id: Book ID

        Raises:
            NotFoundError: If book not found
        """
        self.repository.delete(book_id)
        self.logger.info(f"Deleted book with ID: {book_id}")


class BookAPI:
    """REST API controller for books."""

    def __init__(self, app: Flask, service: BookService):
        """Initialize API.

        Args:
            app: Flask application
            service: Book service instance
        """
        self.app = app
        self.service = service
        self.logger = logging.getLogger(self.__class__.__name__)
        self._register_routes()

    def _register_routes(self) -> None:
        """Register API routes."""
        self.app.route("/health", methods=["GET"])(self._health_check)
        self.app.route("/books", methods=["GET"])(self._list_books)
        self.app.route("/books", methods=["POST"])(self._create_book)
        self.app.route("/books/<int:book_id>", methods=["GET"])(self._get_book)
        self.app.route("/books/<int:book_id>", methods=["PUT"])(self._update_book)
        self.app.route("/books/<int:book_id>", methods=["DELETE"])(self._delete_book)

        # Error handlers
        self.app.errorhandler(404)(self._handle_404)
        self.app.errorhandler(500)(self._handle_500)

    def _health_check(self):
        """Health check endpoint.

        Returns:
            JSON status response
        """
        self.logger.debug("Health check requested")
        return jsonify({"status": "healthy"}), 200

    def _list_books(self):
        """List all books.

        Returns:
            JSON array of books
        """
        try:
            books = self.service.get_all_books()
            return jsonify({"books": [b.to_dict() for b in books]}), 200
        except Exception as e:
            self.logger.error(f"Error listing books: {str(e)}")
            return jsonify({"error": str(e)}), 500

    def _create_book(self):
        """Create new book.

        Returns:
            JSON with created book
        """
        try:
            if not request.is_json:
                return jsonify({"error": "Request must be JSON"}), 400

            book = self.service.create_book(request.get_json())
            return jsonify(book.to_dict()), 201

        except ValidationError as e:
            self.logger.warning(f"Validation error: {str(e)}")
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            self.logger.error(f"Error creating book: {str(e)}")
            return jsonify({"error": str(e)}), 500

    def _get_book(self, book_id: int):
        """Get specific book.

        Args:
            book_id: Book ID

        Returns:
            JSON with book data
        """
        try:
            book = self.service.get_book(book_id)
            return jsonify(book.to_dict()), 200
        except NotFoundError as e:
            self.logger.warning(f"Book not found: {str(e)}")
            return jsonify({"error": str(e)}), 404
        except Exception as e:
            self.logger.error(f"Error getting book: {str(e)}")
            return jsonify({"error": str(e)}), 500

    def _update_book(self, book_id: int):
        """Update book.

        Args:
            book_id: Book ID

        Returns:
            JSON with updated book
        """
        try:
            if not request.is_json:
                return jsonify({"error": "Request must be JSON"}), 400

            book = self.service.update_book(book_id, request.get_json())
            return jsonify(book.to_dict()), 200

        except ValidationError as e:
            self.logger.warning(f"Validation error: {str(e)}")
            return jsonify({"error": str(e)}), 400
        except NotFoundError as e:
            self.logger.warning(f"Book not found: {str(e)}")
            return jsonify({"error": str(e)}), 404
        except Exception as e:
            self.logger.error(f"Error updating book: {str(e)}")
            return jsonify({"error": str(e)}), 500

    def _delete_book(self, book_id: int):
        """Delete book.

        Args:
            book_id: Book ID

        Returns:
            JSON success message
        """
        try:
            self.service.delete_book(book_id)
            return jsonify({"message": f"Book {book_id} deleted"}), 200
        except NotFoundError as e:
            self.logger.warning(f"Book not found: {str(e)}")
            return jsonify({"error": str(e)}), 404
        except Exception as e:
            self.logger.error(f"Error deleting book: {str(e)}")
            return jsonify({"error": str(e)}), 500

    @staticmethod
    def _handle_404(error):
        """Handle 404 errors.

        Args:
            error: Error object

        Returns:
            JSON error response
        """
        logger.warning(f"404 Not Found: {request.path}")
        return jsonify({"error": "Endpoint not found"}), 404

    @staticmethod
    def _handle_500(error):
        """Handle 500 errors.

        Args:
            error: Error object

        Returns:
            JSON error response
        """
        logger.error(f"500 Internal Server Error: {str(error)}")
        return jsonify({"error": "Internal server error"}), 500


def create_app() -> Flask:
    """Factory function to create Flask application.

    Returns:
        Configured Flask app
    """
    app = Flask(__name__)

    # Initialize dependencies
    repository = InMemoryRepository()
    validator = BookValidator()
    service = BookService(repository, validator)

    # Initialize API
    BookAPI(app, service)

    logger.info("REST API (with OOP) initialized")
    return app


if __name__ == "__main__":
    app = create_app()
    logger.info("Starting REST API (with OOP)")
    app.run(debug=True, port=5001)

