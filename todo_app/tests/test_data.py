from datetime import datetime, timedelta

from todo_app.trello.trello_item import TrelloItem
from todo_app.trello.trello_list import TrelloList
from todo_app.trello.trello_base  import TrelloBase

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

def get_test_trello_list():
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
    return trello_list