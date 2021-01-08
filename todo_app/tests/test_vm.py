from todo_app.trello.trello_item import TrelloItem
import pytest

from todo_app.data.trello_items import get_all_trello_items
from todo_app.view_models.trello_view_model import TrelloViewModel
from todo_app.trello.trello_list import TrelloList
from todo_app.trello.trello_base  import TrelloBase

@pytest.fixture
def tvm() -> TrelloViewModel:
    TrelloBase.todo_list_id = 1
    TrelloBase.done_list_id = 2
    TrelloBase.doing_list_id = 3

    trello_list = TrelloList()  
    trello_list.add(TrelloItem(1,'Get Banana',TrelloBase.get_done_list_id()))
    trello_list.add(TrelloItem(2,'Get Apple',TrelloBase.get_done_list_id()))
    trello_list.add(TrelloItem(3,'Get Pear',TrelloBase.get_done_list_id()))
    
    trello_list.add(TrelloItem(4,'Get Ford',TrelloBase.get_todo_list_id()))
    trello_list.add(TrelloItem(5,'Get Ferrari',TrelloBase.get_todo_list_id()))

    trello_list.add(TrelloItem(6,'Get Piper',TrelloBase.get_doing_list_id()))

    return TrelloViewModel(trello_list)


def test_get_todo_items(tvm):
    l = tvm.get_todo_items()
    assert l.len == 2

def test_get_doing_items(tvm):
    l = tvm.get_doing_items()
    assert l.len == 1

def test_get_done_items(tvm):
    l = tvm.get_done_items()
    assert l.len == 3


