import pytest
from datetime import datetime, timedelta

from todo_app.trello.trello_item import TrelloItem
from todo_app.trello.trello_list import TrelloList
from todo_app.trello.trello_base  import TrelloBase
from todo_app.view_models.trello_view_model import TrelloViewModel

@pytest.fixture
def tvm() -> TrelloViewModel:
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

    return TrelloViewModel(trello_list)


def test_get_todo_items(tvm):
    l = tvm.get_todo_items()
    assert l.len == 2

def test_get_doing_items(tvm):
    l = tvm.get_doing_items()
    assert l.len == 5

def test_get_done_items(tvm):
    l = tvm.get_done_items()
    assert l.len == 4

def test_get_items_done_today(tvm):
    l = tvm.get_items_done_today()
    assert l.len == 3

def test_get_items_done_before_today(tvm):
    l = tvm.get_items_done_before_today()
    assert l.len == 1

