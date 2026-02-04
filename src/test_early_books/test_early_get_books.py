import pytest
from fastapi.testclient import TestClient
from fastapienv.books import app

@pytest.fixture(scope="class")
def client():
    """Fixture to provide a TestClient for the FastAPI app."""
    with TestClient(app) as c:
        yield c

class TestGetBooks:
    @pytest.mark.happy_path
    def test_root_returns_all_books(self, client):
        """Test that GET / returns the complete list of books."""
        response = client.get("/")
        assert response.status_code == 200
        books = response.json()
        assert isinstance(books, list)
        assert len(books) == 6
        # Check that all expected keys are present in each book
        for book in books:
            assert set(book.keys()) == {"title", "author", "category"}

    @pytest.mark.happy_path
    def test_my_book_endpoint(self, client):
        """Test that GET /books/my_book returns the favorite book."""
        response = client.get("/books/my_book")
        assert response.status_code == 200
        data = response.json()
        assert data == {"title": "My favorite book"}

    @pytest.mark.happy_path
    def test_dynamic_param_endpoint(self, client):
        """Test that GET /books/{dynamic_param} returns the correct dynamic_param."""
        response = client.get("/books/12345")
        assert response.status_code == 200
        data = response.json()
        assert data == {"dynamic_param": "12345"}

    @pytest.mark.edge_case
    def test_dynamic_param_with_special_characters(self, client):
        """Test that GET /books/{dynamic_param} handles special characters."""
        special_param = "some%20book%2Fwith%3Fchars"
        response = client.get(f"/books/{special_param}")
        assert response.status_code == 200
        data = response.json()
        # URL decoding should occur
        assert data == {"dynamic_param": "some book/with?chars"}

    @pytest.mark.edge_case
    def test_dynamic_param_with_empty_string(self, client):
        """Test that GET /books/ with empty dynamic_param returns 404 (route not matched)."""
        response = client.get("/books/")
        # FastAPI does not match this route, should return 404
        assert response.status_code == 404

    @pytest.mark.edge_case
    def test_nonexistent_route(self, client):
        """Test that a completely invalid route returns 404."""
        response = client.get("/nonexistent")
        assert response.status_code == 404

    @pytest.mark.edge_case
    def test_method_not_allowed(self, client):
        """Test that POST to / is not allowed (only GET is defined)."""
        response = client.post("/")
        assert response.status_code == 405

    @pytest.mark.edge_case
    def test_case_sensitivity_of_routes(self, client):
        """Test that route matching is case-sensitive."""
        response = client.get("/BOOKS/my_book")
        assert response.status_code == 404

    @pytest.mark.edge_case
    def test_dynamic_param_with_unicode(self, client):
        """Test that GET /books/{dynamic_param} handles unicode characters."""
        unicode_param = "书本"
        response = client.get(f"/books/{unicode_param}")
        assert response.status_code == 200
        data = response.json()
        assert data == {"dynamic_param": unicode_param}