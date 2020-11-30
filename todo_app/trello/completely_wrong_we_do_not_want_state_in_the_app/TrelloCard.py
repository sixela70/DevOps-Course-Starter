from .TrelloBase import TrelloBase

class TrelloCard(TrelloBase):

    def __init__(self, id, name, parent_id):
        self.id = id
        self.name = name
        self.parent_id = parent_id

    @classmethod 
    def populate(cls,id,name,list_id):
        new_card = TrelloCard(id,name,list_id)
        return new_card

    def move_list(self, newlist):
        #TODO API CALL to MOVE LIST
        self.mylist = newlist
        



