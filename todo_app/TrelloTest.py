import requests
import os
from trello.trello_base import TrelloBase
from data.trello_items import get_board_id,get_items,get_todo_list_id,get_done_list_id,get_items

#if __name__ == "__main__":
 #   pass
#my_board = TrelloBoard.get_my_board()

#my_board.print()


def main():
    #for k, v in os.environ.items():
    #    print(f'{k}={v}')
    #print("hello world")
    #my_board = TrelloBoard.get_my_board()
    #TrelloBase.init_keys("trello.secrets")
    #print(os.environ)
    TrelloBase.init_keys()
    #print(TrelloBase.auth_tokens())
    print(get_board_id())
    get_items()
    print(get_todo_list_id())
    print(get_done_list_id())

    list = get_items()


if __name__ == "__main__":
    main()