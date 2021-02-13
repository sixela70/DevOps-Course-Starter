import os
import requests
 
class TrelloBase:

    init = False
    developer_api_key = "a key"
    my_secret = "a secret"
    server_token = "a token"
    base_address="https://api.trello.com/1/"
    board_id = None
    todo_list_id = None
    done_list_id = None
    doing_list_id = None
       
    @classmethod
    def init_keys(cls):
        TrelloBase.developer_api_key = os.environ['DEVELOPER_API_KEY']
        TrelloBase.my_secret = os.environ['MY_SECRET']
        TrelloBase.server_token = os.environ['SERVER_TOKEN']
        TrelloBase.board_id = os.environ['TRELLO_BOARD_ID']

    @classmethod
    def auth_tokens(cls):
        if TrelloBase.init == False:
            TrelloBase.init_keys()
            TrelloBase.init = True

        return '&key='+TrelloBase.developer_api_key+'&token='+TrelloBase.server_token

    @classmethod
    def auth_tokens_obj(cls):
        if TrelloBase.init == False:
            TrelloBase.init_keys()
            TrelloBase.init = True

        return { 'key' : TrelloBase.developer_api_key, 'token' : TrelloBase.server_token }
    
    @classmethod
    def get_board_id(cls):
        if TrelloBase.board_id is None:
            url = 'https://api.trello.com/1/members/me/boards?fields=id'+TrelloBase.auth_tokens()
            response= requests.get(url)
            jsonResponse = response.json()
            TrelloBase.board_id = jsonResponse[0]['id'] # Do not like this does not feel safe
        return TrelloBase.board_id

    @classmethod
    def get_lists(cls):
        board_id = TrelloBase.get_board_id()
        url = TrelloBase.base_address+'boards/'+board_id+'/lists?fields=id,name'+TrelloBase.auth_tokens()
        response= requests.get(url)
        return response.json()

    @classmethod
    def get_todo_list_id(cls):
        if TrelloBase.todo_list_id is None:
            jsonResponse = TrelloBase.get_lists()
            for item in jsonResponse:
                if item['name'] == 'ToDoList':
                     TrelloBase.todo_list_id = item['id']
        return TrelloBase.todo_list_id            

    @classmethod
    def get_done_list_id(cls):
        if TrelloBase.done_list_id is None:
            jsonResponse = TrelloBase.get_lists()
            for item in jsonResponse:
                if item['name'] == 'DoneList':
                    TrelloBase.done_list_id = item['id']
        return TrelloBase.done_list_id            

    @classmethod
    def get_doing_list_id(cls):
        if TrelloBase.doing_list_id is None:
            jsonResponse = TrelloBase.get_lists()
            for item in jsonResponse:
                if item['name'] == 'Doing':
                    TrelloBase.doing_list_id = item['id']
        return TrelloBase.doing_list_id            

