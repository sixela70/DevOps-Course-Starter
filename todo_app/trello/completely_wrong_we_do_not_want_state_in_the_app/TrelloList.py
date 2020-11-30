
import requests
from .TrelloBase import TrelloBase
from .TrelloCard import TrelloCard

class TrelloList(TrelloBase):

    branch_url = "lists/"
     
    @classmethod
    def get_list_url(cls, filter):
        url = TrelloBase.base_address+TrelloList.branch_url+filter+TrelloBase.auth_tokens()
        print('Request URL :' + url)
        return url

    def __init__(self, id, name, parent_id):     
        self.id = id
        self.name = name
        self.parent_id = parent_id
        self.cards = []

    # Get all the Cards in the List 
    @classmethod 
    def populate(cls,id,name,board_id):
        new_list = TrelloList(id,name,board_id)
        url = TrelloList.get_list_url(id+'/cards?')
        response= requests.get(url)
        jsonResponse = response.json()        
        for item in jsonResponse:
            new_card = TrelloCard.populate(item['id'],item['name'],id)
            new_list.cards.append(new_card)
        return new_list

    #def create_card(self,name):
    #    new_card = TrelloCard.create(name,id)
    #    self.add_card(new_card)
    #    return new_card

    #def take_card(self, trello_card):
    #    self.cards.append(trello_card)
    #    #TODO WEB call to take card not sure if cards can me moved . 

    #querystring = {"name": card_name, "idList": list_id, "key": key, "token": token}
    #response = requests.request("POST", url, params=querystring)
    #card_id = response.json()["id"]
    #return card_id




