import pytest
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_gists_octocat(client):
    """Validate that we can fetch gists for the octocat user."""
    response = client.get('/octocat')
    assert response.status_code == 200
    assert isinstance(response.json, list)
    # octocat usually has public gists, let's verify if data exists
    if len(response.json) > 0:
        assert 'html_url' in response.json[0]

def test_user_not_found(client):
    """Validate behavior for a likely non-existent user."""
    response = client.get('/this-user-should-not-exist-123456789')
    assert response.status_code == 404

def test_pagination(client):
    """Verify that pagination parameters are accepted."""
    # Requesting 1 item per page
    response = client.get('/octocat?per_page=1&page=1')
    assert response.status_code == 200
    # Remove the () after .json
    assert len(response.json) <= 1

def test_caching_headers(client):
    """Verify the app responds correctly (basic smoke test)."""
    response = client.get('/octocat')
    assert response.status_code == 200