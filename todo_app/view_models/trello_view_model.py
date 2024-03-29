

from todo_app.trello.trello_item import TrelloItem
from todo_app.trello.trello_list import TrelloList


class TrelloViewModel:
    
    def __init__(self, trello_items_list):
        self._items=trello_items_list

    @property
    def items(self):
        return self._items

    def filter_items(self, filter):
        l = TrelloList()
        for item in self._items.trello_items:
            if filter(item):
                l.add(item) 
        return l

    def get_todo_items(self):
        return self.filter_items(TrelloItem.isToDo)

    def get_doing_items(self):
        return self.filter_items(TrelloItem.isDoing)

    def show_all_done_items(self):
        return self.filter_items(TrelloItem.isDone)       

    def recent_done_items(self):
       return self.filter_items(TrelloItem.isDoneToday)       

    def older_done_items(self):        
        return self.filter_items(TrelloItem.wasDoneBeforeToday)  
