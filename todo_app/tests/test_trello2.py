import pytest
from todo_app.trello.trello_api2 import TrelloAPI2
from todo_app.trello.trello_base  import TrelloBase
from dotenv import load_dotenv, find_dotenv

@pytest.fixture(scope='module')
def init_env():
    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)

@pytest.fixture
def tapi() -> TrelloAPI2:
        return TrelloAPI2()


def test_enironment_has_been_read(init_env):
        assert TrelloBase.get_board_id() != None
        assert TrelloBase.get_done_list_id() != None
        assert TrelloBase.get_todo_list_id() != None

def test_get_trello_list(init_env,tapi):
        trello_list = tapi.get_all_trello_items()

def test_create_delete_trello_board(init_env,tapi):
        new_board_id = tapi.create_trello_board('unit test board')
        assert new_board_id != None
        assert Tapi.delete_trello_board(new_board_id) == 200



