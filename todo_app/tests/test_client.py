import pytest
from dotenv import load_dotenv, find_dotenv
from todo_app.app import create_app

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    test_app = create_app()

    with test_app.test_client() as client:
        yield client


# I think this is what I am being asked to do 
# So we need to mock the response from Trello for our initial page load. 
# Best way to do this is to grab the actual json returned from our trello request save it an inject it. 

# So I want to replace my TrelloAPI with a MOCK TrelloAPI that reutrnsd static values 





#@pytest.fixture


#def mock_get_request():

#def test_index_page(mock_get_request, client):
#    response = client.get('/')


#def test_index_page(client):
#    response = client.get('/')
#    assert response != None


