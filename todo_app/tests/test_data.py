from datetime import datetime, timedelta

from todo_app.data.item import Item

get_banana = Item(10,'Get Banana',"Done",datetime.now()) 
get_apple = Item(12,'Get Apple',"Done",datetime.now())
get_pear = Item(13,'Get Pear',"Done",datetime.now())
get_ford = Item(24,'Get Ford',"ToDo",datetime.now())
get_ferrari = Item(25,'Get Ferrari',"ToDo",datetime.now())
get_rambutans = Item(37,'Get Rambutans',"Done", datetime.now() - timedelta(1))
get_piper_1 = Item(61,'Get Piper 1',"Doing",datetime.now())
get_piper_2 = Item(62,'Get Piper 2',"Doing",datetime.now())
get_piper_3 = Item(63,'Get Piper 3',"Doing",datetime.now())
get_piper_4 = Item(64,'Get Piper 4',"Doing",datetime.now())
get_piper_5 = Item(65,'Get Piper 5',"Doing",datetime.now())

def get_test_item_list():
    list = [] 
    list.append( get_banana )
    list.append( get_apple )
    list.append( get_pear )
    list.append( get_ford )
    list.append( get_ferrari )
    list.append( get_rambutans )
    list.append( get_piper_1)
    list.append( get_piper_2)
    list.append( get_piper_3)
    list.append( get_piper_4)
    list.append( get_piper_5)
    return list