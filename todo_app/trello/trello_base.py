import os
import requests
from dotenv import load_dotenv, find_dotenv

class TrelloBase:

    init = False
    developer_api_key = "a key"
    my_secret = "a secret"
    server_token = "a token"
    base_address="https://api.trello.com/1/"
    board_id = None
    todo_list_id = None
    done_list_id = None
       
    @classmethod
    def init_keys(cls):
        #If the environment variables have not been set then try and read .env file 
        #Flask by default reads in .env file 
        if 'DEVELOPER_API_KEY' not in os.environ or 'MY_SECRET' not in os.environ or 'SERVER_TOKEN' not in os.environ:
            print ('Missing environment variable one of DEVELOPER_API_KEY,MY_SECRET,SERVER_TOKEN trying to read .env')            
            file_path = find_dotenv('.env')
            load_dotenv(file_path, override=True)

        if 'DEVELOPER_API_KEY' not in os.environ or 'MY_SECRET' not in os.environ or 'SERVER_TOKEN' not in os.environ:
            print ('Could not find Missing environment variables..please supply or drop in .env file')            
        else: 
            TrelloBase.developer_api_key = os.environ['DEVELOPER_API_KEY']
            TrelloBase.my_secret = os.environ['MY_SECRET']
            TrelloBase.server_token = os.environ['SERVER_TOKEN']

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
    
    '''
    Will look for board called ToDo from the boards accessable in the Trello account 
    UNLESS
    the environment variable TRELLO_BOARD_ID has been set else where. 
    '''
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


