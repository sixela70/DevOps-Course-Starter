
import requests
from todo_app.trello.trello_list import TrelloList
from todo_app.trello.trello_base import TrelloBase
from todo_app.trello.trello_item import TrelloItem

# Get all cards from todolist 
def get_trello_list():
    board_id = TrelloBase.get_board_id()
    done_list_id = TrelloBase.get_done_list_id()
    dolist_id = TrelloBase.get_todo_list_id()
    trello_list = TrelloList()
    url = TrelloBase.base_address+'boards/'+board_id+'/cards?fields=id,idList,name'+TrelloBase.auth_tokens()
    response= requests.get(url)
    jsonResponse = response.json()
    for item in jsonResponse:
        if item['idList'] == done_list_id:
            list_item = TrelloItem(item['id'],item['name'] ,'Done')
        elif item['idList'] == dolist_id:
            list_item = TrelloItem(item['id'],item['name'] ,'Not Started')
        else:
            print('Discarding items from other test list ' + item['id'] + '  ' +item['name'])
            continue
        trello_list.add(list_item)    
    return trello_list

def get_all_trello_items():
    url = TrelloBase.base_address+'boards/'+TrelloBase.get_board_id()+'/cards?fields=id,idList,name'+TrelloBase.auth_tokens()
    response= requests.get(url)
    jsonResponse = response.json()
    trello_list = TrelloList()
    for item in jsonResponse:
        trello_list.add(TrelloItem(item['id'],item['name'],item['idList']))
    return trello_list

def add_item(title):
    dolist_id = TrelloBase.get_todo_list_id()
    url = TrelloBase.base_address+'/cards?'
    data = TrelloBase.auth_tokens_obj()
    data["idList"] = dolist_id
    data["name"] =  title
    requests.post(url, data)

## Move item to the other list 
def mark_item_done(item):
    markid_item_done(item['id'])

def markid_item_done(id):
    done_list_id = TrelloBase.get_done_list_id()
    url = TrelloBase.base_address+'/cards/'+id+'?'
    data = TrelloBase.auth_tokens_obj()
    data["idList"] = done_list_id
    requests.put(url, data)

def mark_item_not_done(item):
    markid_item_undone(item['id'])
    
def markid_item_undone(id):
    dolist_id = TrelloBase.get_todo_list_id()
    url = TrelloBase.base_address+'/cards/'+id+'?'
    data = TrelloBase.auth_tokens_obj()
    data["idList"] = dolist_id
    requests.put(url, data)
