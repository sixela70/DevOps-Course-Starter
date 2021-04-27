import pytest
from todo_app.trello.trello_api import TrelloAPI
from todo_app.trello.trello_base  import TrelloBase
from dotenv import load_dotenv, find_dotenv

#Check we can sucessfully use our TrelloAPI outside of the flask application. 
@pytest.fixture(scope='module')
def init_env():
    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)

def test_enironment_has_been_read(init_env):
        assert TrelloBase.get_board_id() != None
        assert TrelloBase.get_done_list_id() != None
        assert TrelloBase.get_todo_list_id() != None

def test_get_trello_list(init_env):
        trello_list = TrelloAPI.get_all_trello_items()
        assert trello_list.len != 0

def test_create_delete_trello_board(init_env):
        new_board_id = TrelloAPI.create_trello_board('unit test board')
        assert new_board_id != None
        assert TrelloAPI.delete_trello_board(new_board_id) == 200



