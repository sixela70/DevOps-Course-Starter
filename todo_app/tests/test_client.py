
import pytest
import requests

from lxml import html

from todo_app.tests.test_data import *

from datetime import datetime, timedelta
from dotenv import load_dotenv, find_dotenv
from todo_app.app import create_app
from todo_app.data.mongodb import MongoDb
from todo_app.data.item import Item

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    test_app = create_app()

    with test_app.test_client() as client:
        yield client

def test_index_page(monkeypatch, client):

    def mock_get_all_items():
        list = get_test_item_list()
        return list

    monkeypatch.setattr(MongoDb,"get_all_items", mock_get_all_items)
    
    response = client.get('/')
    assert response.status_code == 200
    tree = html.fromstring(response.data)
    items = tree.xpath('.//div[@class="card_text"]/text()')
    assert ( len(items) == 15 )
    

