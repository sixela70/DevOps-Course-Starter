import pytest
import collections

from datetime import datetime, timedelta

from todo_app.trello.trello_item import TrelloItem
from todo_app.trello.trello_list import TrelloList
from todo_app.trello.trello_base  import TrelloBase
from todo_app.view_models.trello_view_model import TrelloViewModel

TrelloBase.todo_list_id = 1
TrelloBase.done_list_id = 2
TrelloBase.doing_list_id = 3

get_banana = TrelloItem(10,'Get Banana',TrelloBase.get_done_list_id(),datetime.now()) 
get_apple = TrelloItem(12,'Get Apple',TrelloBase.get_done_list_id(),datetime.now())
get_pear = TrelloItem(13,'Get Pear',TrelloBase.get_done_list_id(),datetime.now())
get_ford = TrelloItem(24,'Get Ford',TrelloBase.get_todo_list_id(),datetime.now())
get_ferrari = TrelloItem(25,'Get Ferrari',TrelloBase.get_todo_list_id(),datetime.now())
get_rambutans = TrelloItem(37,'Get Rambutans',TrelloBase.get_done_list_id(), datetime.now() - timedelta(1))
get_piper_1 = TrelloItem(61,'Get Piper 1',TrelloBase.get_doing_list_id(),datetime.now())
get_piper_2 = TrelloItem(62,'Get Piper 2',TrelloBase.get_doing_list_id(),datetime.now())
get_piper_3 = TrelloItem(63,'Get Piper 3',TrelloBase.get_doing_list_id(),datetime.now())
get_piper_4 = TrelloItem(64,'Get Piper 4',TrelloBase.get_doing_list_id(),datetime.now())
get_piper_5 = TrelloItem(65,'Get Piper 5',TrelloBase.get_doing_list_id(),datetime.now())



@pytest.fixture
def tvm() -> TrelloViewModel:

    trello_list = TrelloList()  
    trello_list.add( get_banana )
    trello_list.add( get_apple )
    trello_list.add( get_pear )
    trello_list.add( get_ford )
    trello_list.add( get_ferrari )
    trello_list.add( get_rambutans )
    trello_list.add( get_piper_1)
    trello_list.add( get_piper_2)
    trello_list.add( get_piper_3)
    trello_list.add( get_piper_4)
    trello_list.add( get_piper_5)

    return TrelloViewModel(trello_list)

def test_get_todo_items(tvm):
    trello_list = tvm.get_todo_items()
    assert trello_list.trello_items == [get_ford, get_ferrari]

def test_get_doing_items(tvm):
    l = tvm.get_doing_items()
    assert l.trello_items == [get_piper_1, get_piper_2, get_piper_3, get_piper_4, get_piper_5]

def test_show_all_done_items(tvm):
    l = tvm.show_all_done_items()
    assert l.trello_items == [ get_banana,get_apple, get_pear, get_rambutans ]

def test_get_recent_done_items(tvm):
    l = tvm.recent_done_items()
    assert l.trello_items == [ get_banana,get_apple, get_pear ]

def test_get_older_done_items(tvm):
    l = tvm.older_done_items()
    assert l.trello_items == [ get_rambutans ]

