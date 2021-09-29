import pytest
import collections
import requests
from datetime import datetime, timedelta


from todo_app.tests.test_data import *
from todo_app.data.item import Item
#from todo_app.trello.trello_item import TrelloItem
#from todo_app.trello.trello_list import TrelloList
#from todo_app.trello.trello_base  import TrelloBase
#from todo_app.view_models.trello_view_model import TrelloViewModel

from todo_app.view_models.view_model import ViewModel

@pytest.fixture
def tvm() -> ViewModel:
    list = get_test_item_list()
    return ViewModel(list)

def test_get_todo_items(tvm):
    list = tvm.get_todo_items()
    assert list == [get_ford, get_ferrari ]

def test_get_doing_items(tvm):
    l = tvm.get_doing_items()
    assert l == [get_piper_1, get_piper_2, get_piper_3, get_piper_4, get_piper_5]

def test_show_all_done_items(tvm):
    l = tvm.show_all_done_items()
    assert l == [ get_banana, get_apple, get_pear, get_rambutans ]

def test_get_recent_done_items(tvm):
    l = tvm.recent_done_items()
    assert l == [ get_banana,get_apple, get_pear ]

def test_get_older_done_items(tvm):
    l = tvm.older_done_items()
    assert l == [ get_rambutans ]

