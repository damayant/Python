"""Tests for OOP REST API implementation."""

import pytest
from with_oop.app import (
    Book,
    BookValidator,
    ValidationError,
    InMemoryRepository,
    NotFoundError,
    BookService,
    create_app,
)


class TestBook:
    """Test cases for Book model."""

    def test_book_creation(self):
        """Test creating a book."""
        book = Book(id=1, title="Python 101", author="John Doe", year=2023)
        assert book.id == 1
        assert book.title == "Python 101"
        assert book.author == "John Doe"
        assert book.year == 2023

    def test_book_to_dict(self):
        """Test converting book to dictionary."""
        book = Book(id=1, title="Python 101", author="John Doe", year=2023)
        book_dict = book.to_dict()
        assert book_dict["id"] == 1
        assert book_dict["title"] == "Python 101"
        assert book_dict["author"] == "John Doe"
        assert book_dict["year"] == 2023


class TestBookValidator:
    """Test cases for BookValidator."""

    def test_validate_create_data_valid(self):
        """Test validation with valid data."""
        data = {"title": "Python 101", "author": "John Doe"}
        # Should not raise exception
        BookValidator.validate_create_data(data)

    def test_validate_create_data_missing_field(self):
        """Test validation with missing required field."""
        data = {"title": "Python 101"}
        with pytest.raises(ValidationError):
            BookValidator.validate_create_data(data)

    def test_validate_create_data_empty_string(self):
        """Test validation with empty string."""
        data = {"title": "", "author": "John Doe"}
        with pytest.raises(ValidationError):
            BookValidator.validate_create_data(data)

    def test_validate_create_data_invalid_type(self):
        """Test validation with invalid data type."""
        data = "not a dict"
        with pytest.raises(ValidationError):
            BookValidator.validate_create_data(data)

    def test_validate_update_data_valid(self):
        """Test update validation with valid data."""
        data = {"title": "New Title"}
        BookValidator.validate_update_data(data)

    def test_validate_update_data_empty_title(self):
        """Test update validation with empty title."""
        data = {"title": ""}
        with pytest.raises(ValidationError):
            BookValidator.validate_update_data(data)


class TestInMemoryRepository:
    """Test cases for InMemoryRepository."""

    @pytest.fixture
    def repository(self):
        """Create repository instance."""
        return InMemoryRepository()

    def test_add_book(self, repository):
        """Test adding book to repository."""
        book = Book(id=0, title="Python 101", author="John Doe")
        repository.add(book)
        assert book.id == 1
        assert len(repository.find_all()) == 1

    def test_find_by_id(self, repository):
        """Test finding book by ID."""
        book = Book(id=0, title="Python 101", author="John Doe")
        repository.add(book)
        found_book = repository.find_by_id(1)
        assert found_book is not None
        assert found_book.title == "Python 101"

    def test_find_by_id_not_found(self, repository):
        """Test finding non-existent book."""
        found_book = repository.find_by_id(999)
        assert found_book is None

    def test_find_all(self, repository):
        """Test finding all books."""
        book1 = Book(id=0, title="Book 1", author="Author 1")
        book2 = Book(id=0, title="Book 2", author="Author 2")
        repository.add(book1)
        repository.add(book2)
        books = repository.find_all()
        assert len(books) == 2

    def test_update_book(self, repository):
        """Test updating book."""
        book = Book(id=0, title="Python 101", author="John Doe")
        repository.add(book)
        book.title = "Advanced Python"
        repository.update(book)
        updated_book = repository.find_by_id(1)
        assert updated_book.title == "Advanced Python"

    def test_update_book_not_found(self, repository):
        """Test updating non-existent book."""
        book = Book(id=999, title="Python 101", author="John Doe")
        with pytest.raises(NotFoundError):
            repository.update(book)

    def test_delete_book(self, repository):
        """Test deleting book."""
        book = Book(id=0, title="Python 101", author="John Doe")
        repository.add(book)
        repository.delete(1)
        assert len(repository.find_all()) == 0

    def test_delete_book_not_found(self, repository):
        """Test deleting non-existent book."""
        with pytest.raises(NotFoundError):
            repository.delete(999)


class TestBookService:
    """Test cases for BookService."""

    @pytest.fixture
    def service(self):
        """Create service instance."""
        repository = InMemoryRepository()
        validator = BookValidator()
        return BookService(repository, validator)

    def test_create_book(self, service):
        """Test creating book via service."""
        data = {"title": "Python 101", "author": "John Doe", "year": 2023}
        book = service.create_book(data)
        assert book.id == 1
        assert book.title == "Python 101"
        assert book.year == 2023

    def test_create_book_invalid_data(self, service):
        """Test creating book with invalid data."""
        data = {"title": ""}
        with pytest.raises(ValidationError):
            service.create_book(data)

    def test_get_book(self, service):
        """Test getting book by ID."""
        data = {"title": "Python 101", "author": "John Doe"}
        created_book = service.create_book(data)
        retrieved_book = service.get_book(created_book.id)
        assert retrieved_book.title == "Python 101"

    def test_get_book_not_found(self, service):
        """Test getting non-existent book."""
        with pytest.raises(NotFoundError):
            service.get_book(999)

    def test_get_all_books(self, service):
        """Test getting all books."""
        data1 = {"title": "Book 1", "author": "Author 1"}
        data2 = {"title": "Book 2", "author": "Author 2"}
        service.create_book(data1)
        service.create_book(data2)
        books = service.get_all_books()
        assert len(books) == 2

    def test_update_book(self, service):
        """Test updating book."""
        data = {"title": "Python 101", "author": "John Doe"}
        created_book = service.create_book(data)
        update_data = {"title": "Advanced Python"}
        updated_book = service.update_book(created_book.id, update_data)
        assert updated_book.title == "Advanced Python"
        assert updated_book.author == "John Doe"

    def test_delete_book(self, service):
        """Test deleting book."""
        data = {"title": "Python 101", "author": "John Doe"}
        created_book = service.create_book(data)
        service.delete_book(created_book.id)
        books = service.get_all_books()
        assert len(books) == 0


class TestBookAPI:
    """Test cases for REST API."""

    @pytest.fixture
    def client(self):
        """Create Flask test client."""
        app = create_app()
        app.config["TESTING"] = True
        return app.test_client()

    def test_health_check(self, client):
        """Test health check endpoint."""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json["status"] == "healthy"

    def test_list_books_empty(self, client):
        """Test listing books when none exist."""
        response = client.get("/books")
        assert response.status_code == 200
        assert response.json["books"] == []

    def test_create_book(self, client):
        """Test creating book via API."""
        data = {"title": "Python 101", "author": "John Doe", "year": 2023}
        response = client.post("/books", json=data)
        assert response.status_code == 201
        assert response.json["title"] == "Python 101"
        assert response.json["id"] == 1

    def test_create_book_invalid_json(self, client):
        """Test creating book with invalid JSON."""
        response = client.post("/books", data="invalid")
        assert response.status_code == 400

    def test_create_book_missing_field(self, client):
        """Test creating book with missing field."""
        data = {"title": "Python 101"}
        response = client.post("/books", json=data)
        assert response.status_code == 400

    def test_get_book(self, client):
        """Test getting specific book."""
        # Create book first
        create_data = {"title": "Python 101", "author": "John Doe"}
        create_response = client.post("/books", json=create_data)
        book_id = create_response.json["id"]

        # Get book
        response = client.get(f"/books/{book_id}")
        assert response.status_code == 200
        assert response.json["title"] == "Python 101"

    def test_get_book_not_found(self, client):
        """Test getting non-existent book."""
        response = client.get("/books/999")
        assert response.status_code == 404

    def test_update_book(self, client):
        """Test updating book."""
        # Create book
        create_data = {"title": "Python 101", "author": "John Doe"}
        create_response = client.post("/books", json=create_data)
        book_id = create_response.json["id"]

        # Update book
        update_data = {"title": "Advanced Python"}
        response = client.put(f"/books/{book_id}", json=update_data)
        assert response.status_code == 200
        assert response.json["title"] == "Advanced Python"

    def test_delete_book(self, client):
        """Test deleting book."""
        # Create book
        create_data = {"title": "Python 101", "author": "John Doe"}
        create_response = client.post("/books", json=create_data)
        book_id = create_response.json["id"]

        # Delete book
        response = client.delete(f"/books/{book_id}")
        assert response.status_code == 200

        # Verify deleted
        get_response = client.get(f"/books/{book_id}")
        assert get_response.status_code == 404

