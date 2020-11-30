import os
 
class TrelloBase:

    init = False
    developer_api_key = "a key"
    my_secret = "a secret"
    server_token = "a token"

    #developer_api_key="2bf28cd9609b6d82c6accd4fa78be70c"
    #my_Secret="526dac3e066c92f0e02701bf983246e6a0aea2b065f516055e0f7e5098700caf"
    #server_token="94027d7e2a6eedb95e62a24826ae1eff2d074717a7db7e1c0b108210813c3cfa"
    #base_address="https://api.trello.com/1/members/me/"
    base_address="https://api.trello.com/1/"

    @classmethod
    def init_keys(cls):
        TrelloBase.developer_api_key = os.environ['DEVELOPER_API_KEY']
        TrelloBase.my_secret = os.environ['MY_SECRET']
        TrelloBase.server_token = os.environ['SERVER_TOKEN']
    
    @classmethod
    def auth_tokens(cls):
        
        if TrelloBase.init == False:
            TrelloBase.init_keys()
            TrelloBase.init = True

        return '&key='+TrelloBase.developer_api_key+'&token='+TrelloBase.server_token



