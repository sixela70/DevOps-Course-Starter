
from todo_app.data.item import Item

class ViewModel:
    
    def __init__(self, items_list):
        self._items=items_list

    @property
    def items(self):
        return self._items

    def filter_items(self, filter):
        l =[]
        for item in self._items:
            if filter(item):
                l.append(item) 
        return l

    def get_todo_items(self):
        return self.filter_items(Item.isToDo)

    def get_doing_items(self):
        return self.filter_items(Item.isDoing)

    def show_all_done_items(self):
        return self.filter_items(Item.isDone)       

    def recent_done_items(self):
       return self.filter_items(Item.isDoneToday)       

    def older_done_items(self):        
        return self.filter_items(Item.wasDoneBeforeToday)  
