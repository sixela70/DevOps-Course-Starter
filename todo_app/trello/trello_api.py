
import requests
from datetime import datetime
from todo_app.trello.trello_list import TrelloList
from todo_app.trello.trello_base import TrelloBase
from todo_app.trello.trello_item import TrelloItem

DATE_FORMAT = '%Y-%m-%dT%H:%M:%S.%fz'

class TrelloAPI:

    @classmethod
    def to_trello_item(cls, item, status = None):
        return TrelloItem(item['id'],item['name'],item['idList'],datetime.strptime(item['dateLastActivity'], DATE_FORMAT),status)

    # Get all cards from todolist 
    @classmethod
    def get_trello_list(cls): 
        done_list_id = TrelloBase.get_done_list_id()
        dolist_id = TrelloBase.get_todo_list_id()
        trello_list = TrelloList()
        url = TrelloBase.base_address+'boards/'+TrelloBase.get_board_id()+'/cards?fields=id,idList,name,dateLastActivity'+TrelloBase.auth_tokens()
        response= requests.get(url)
        jsonResponse = response.json()
        for item in jsonResponse:
            if item['idList'] == done_list_id:
                ti = cls.to_trello_item(item,'Done')
            elif item['idList'] == dolist_id:
                ti = cls.to_trello_item(item,'Not Started')
            else:
                print('Discarding items from other test list ' + item['id'] + '  ' +item['name'])
                continue
            trello_list.add(ti)    
        return trello_list

    @classmethod
    def get_all_trello_items(cls):
        url = TrelloBase.base_address+'boards/'+TrelloBase.get_board_id()+'/cards?fields=id,idList,name,dateLastActivity'+TrelloBase.auth_tokens()
        response= requests.get(url)
        jsonResponse = response.json()
        trello_list = TrelloList()
        for item in jsonResponse:
            trello_list.add(cls.to_trello_item(item))
        return trello_list

    @classmethod
    def add_item(cls,title):
        dolist_id = TrelloBase.get_todo_list_id()
        url = TrelloBase.base_address+'/cards?'
        data = TrelloBase.auth_tokens_obj()
        data["idList"] = dolist_id
        data["name"] =  title
        requests.post(url, data)

    ## Move item to the other list 
    @classmethod
    def mark_item_done(cls,item):
        cls.markid_item_done(item['id'])

    @classmethod 
    def markid_item_done(cls,id):
        done_list_id = TrelloBase.get_done_list_id()
        url = TrelloBase.base_address+'/cards/'+id+'?'
        data = TrelloBase.auth_tokens_obj()
        data["idList"] = done_list_id
        requests.put(url, data)

    @classmethod
    def mark_item_not_done(cls,item):
        cls.markid_item_undone(item['id'])

    @classmethod    
    def markid_item_undone(cls,id):
        dolist_id = TrelloBase.get_todo_list_id()
        url = TrelloBase.base_address+'/cards/'+id+'?'
        data = TrelloBase.auth_tokens_obj()
        data["idList"] = dolist_id
        requests.put(url, data)
