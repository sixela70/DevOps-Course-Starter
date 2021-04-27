import pytest
import requests

from lxml import html
from todo_app.trello.trello_base import TrelloBase
from todo_app.trello.trello_list import TrelloList
from todo_app.trello.trello_item import TrelloItem
from todo_app.trello.trello_api import TrelloAPI

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
        TrelloBase.todo_list_id = 1
        TrelloBase.done_list_id = 2
        TrelloBase.doing_list_id = 3

        trello_list = TrelloList()  
        trello_list.add(TrelloItem(10,'Get Banana',TrelloBase.get_done_list_id(),datetime.now()))
        trello_list.add(TrelloItem(12,'Get Apple',TrelloBase.get_done_list_id(),datetime.now()))
        trello_list.add(TrelloItem(13,'Get Pear',TrelloBase.get_done_list_id(),datetime.now()))
        
        trello_list.add(TrelloItem(24,'Get Ford',TrelloBase.get_todo_list_id(),datetime.now()))
        trello_list.add(TrelloItem(25,'Get Ferrari',TrelloBase.get_todo_list_id(),datetime.now()))

        trello_list.add( TrelloItem(37,'Get Rambutans',TrelloBase.get_done_list_id(), datetime.now() - timedelta(1) ))

        trello_list.add(TrelloItem(61,'Get Piper 1',TrelloBase.get_doing_list_id(),datetime.now()))
        trello_list.add(TrelloItem(62,'Get Piper 2',TrelloBase.get_doing_list_id(),datetime.now()))
        trello_list.add(TrelloItem(63,'Get Piper 3',TrelloBase.get_doing_list_id(),datetime.now()))
        trello_list.add(TrelloItem(64,'Get Piper 4',TrelloBase.get_doing_list_id(),datetime.now()))
        trello_list.add(TrelloItem(65,'Get Piper 5',TrelloBase.get_doing_list_id(),datetime.now()))
        return trello_list

    monkeypatch.setattr(TrelloAPI,"get_all_trello_items", mock_get_all_trello_items)
    
    response = client.get('/')
    assert response.status_code == 200
    tree = html.fromstring(response.data)
    items = tree.xpath('.//div[@class="card_text"]/text()')
    assert ( len(items) == 15 )
    

