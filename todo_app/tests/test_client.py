import pytest
import requests

from lxml import html
from todo_app.trello.trello_base import TrelloBase
from todo_app.trello.trello_list import TrelloList
from todo_app.trello.trello_item import TrelloItem
from todo_app.trello.trello_api import TrelloAPI
from todo_app.tests.test_data import *

from datetime import datetime, timedelta
from dotenv import load_dotenv, find_dotenv
from todo_app.app import create_app

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    test_app = create_app()

    with test_app.test_client() as client:
        yield client

def test_index_page(monkeypatch, client):

    def mock_get_all_trello_items():
        trello_list = get_test_trello_list()
        return trello_list

    monkeypatch.setattr(TrelloAPI,"get_all_trello_items", mock_get_all_trello_items)
    
    response = client.get('/')
    assert response.status_code == 200
    tree = html.fromstring(response.data)
    items = tree.xpath('.//div[@class="card_text"]/text()')
    assert ( len(items) == 15 )
    

