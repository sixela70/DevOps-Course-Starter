
# Holds a dicionary of trello items 

class TrelloList:

    def __init__(self):
        self._items=[]

    def add(self,trello_item):
        self._items.append(trello_item)

    @property
    def trello_items(self):
        return self._items 

    @property
    def len(self):
        return len(self._items)
