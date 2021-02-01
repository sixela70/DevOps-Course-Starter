import pytest
from dotenv import load_dotenv, find_dotenv
from todo_app.app import create_app

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test.')
    load_dotenv(file_path, override=True)

    test_app = create_app()

    with test_app.test_client() as client:
        yield client

#@pytest.fixture
#def mock_get_request():


#def test_index_page(mock_get_request, client):
#    response = client.get('/')


def test_index_page(client):
    response = client.get('/')
    assert response != None


