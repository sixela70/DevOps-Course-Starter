import requests
from datetime import datetime
from todo_app.trello.trello_list import TrelloList
from todo_app.trello.trello_base import TrelloBase
from todo_app.trello.trello_item import TrelloItem

DATE_FORMAT = '%Y-%m-%dT%H:%M:%S.%fz'

class TrelloAPI2:

    def get_all_trello_items(self):
        url = TrelloBase.base_address+'boards/'+TrelloBase.get_board_id()+'/cards?fields=id,idList,name,dateLastActivity'+TrelloBase.auth_tokens()
        response= requests.get(url)
        jsonResponse = response.json()
        trello_list = TrelloList()
        for item in jsonResponse:
            trello_list.add(self.to_trello_item(item))
        return trello_list

    def to_trello_item(self, item, status = None):
        return TrelloItem(item['id'],item['name'],item['idList'],datetime.strptime(item['dateLastActivity'], DATE_FORMAT),status)

    def create_trello_board(self, name):
        url = TrelloBase.base_address+'boards/'
        query = TrelloBase.auth_tokens_obj()
        query["name"] = name
        response= requests.post(url,params = query)
        print(response.text)
        jsonResponse = response.json()
        print (jsonResponse['id'])
        return jsonResponse['id']

    
    def delete_trello_board(self, board_id):
        url = TrelloBase.base_address+'boards/'+board_id
        query = TrelloBase.auth_tokens_obj()
        response= requests.delete(url,params = query)
        return response.status_code
        
    
    
    # Get all cards from todolist 
    def get_trello_list(self): 
        done_list_id = TrelloBase.get_done_list_id()
        dolist_id = TrelloBase.get_todo_list_id()
        trello_list = TrelloList()
        url = TrelloBase.base_address+'boards/'+TrelloBase.get_board_id()+'/cards?fields=id,idList,name,dateLastActivity'+TrelloBase.auth_tokens()
        response= requests.get(url)
        jsonResponse = response.json()
        for item in jsonResponse:
            if item['idList'] == done_list_id:
                ti = self.to_trello_item(item,'Done')
            elif item['idList'] == dolist_id:
                ti = to_trello_item(item,'Not Started')
            else:
                print('Discarding items from other test list ' + item['id'] + '  ' +item['name'])
                continue
            trello_list.add(ti)    
        return trello_list

    def add_item(self, title):
        dolist_id = TrelloBase.get_todo_list_id()
        url = TrelloBase.base_address+'/cards?'
        data = TrelloBase.auth_tokens_obj()
        data["idList"] = dolist_id
        data["name"] =  title
        requests.post(url, data)

    ## Move item to the other list 
    def mark_item_doing(self, item):
        self.markid_item_done(item['id'])

    def markid_item_doing(self, id):
        doing_list_id = TrelloBase.get_doing_list_id()
        print(doing_list_id)
        print('doing ')
        url = TrelloBase.base_address+'/cards/'+id+'?'
        data = TrelloBase.auth_tokens_obj()
        data["idList"] = doing_list_id
        requests.put(url, data)

    ## Move item to the other list 
    def mark_item_done(self,item):
        self.markid_item_done(item['id'])

    def markid_item_done(self,id):
        done_list_id = TrelloBase.get_done_list_id()
        url = TrelloBase.base_address+'/cards/'+id+'?'
        data = TrelloBase.auth_tokens_obj()
        data["idList"] = done_list_id
        requests.put(url, data)
    
    def mark_item_not_done(self,item):
        self.markid_item_undone(item['id'])

    def markid_item_undone(self,id):
        dolist_id = TrelloBase.get_todo_list_id()
        url = TrelloBase.base_address+'/cards/'+id+'?'
        data = TrelloBase.auth_tokens_obj()
        data["idList"] = dolist_id
        requests.put(url, data)
