
import requests
from todo_app.trello.trello_base import TrelloBase

# Get all cards from todolist 
def get_items():
    board_id = TrelloBase.get_board_id()
    done_list_id = TrelloBase.get_done_list_id()
    dolist_id = TrelloBase.get_todo_list_id()
    list_items = []
    url = TrelloBase.base_address+'boards/'+board_id+'/cards?fields=id,idList,name'+TrelloBase.auth_tokens()
    response= requests.get(url)
    jsonResponse = response.json()
    ## cycle through and build new list using the list id determine if done or todo yuck yuck yuck why am creating a new list 
    ## surely I can filter in someway .. but I want the status field. 
    ## perhaps if I have time come back to this 
    for item in jsonResponse:
        if item['idList'] == done_list_id:
            list_item = { 'id' : item['id'], 'title' : item['name'] , 'status' : 'Done' }
        elif item['idList'] == dolist_id:
            list_item = { 'id' : item['id'], 'title' : item['name'] , 'status' : 'Not Started' }
        else:
            print('Discarding items from other test list ' + item['id'] + '  ' +item['name'])
        list_items.append(list_item)        
    return list_items

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
