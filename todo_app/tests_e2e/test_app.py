import pytest
import os 

from todo_app.app import create_app
from todo_app.trello.trello_api import TrelloAPI
from todo_app.trello.trello_api import TrelloBase
from selenium import webdriver
from threading import Thread

@pytest.fixture(scope='module')
def test_app():    
    # Create the new board and update the board id environment variable
    TrelloBase.board_id  = TrelloAPI.create_trello_board("E2E test Board")

    # construct the new application                                                                                 
    application = create_app()

    #start the app in its own thread
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield application

    #Tear Down
    thread.join(1)
    TrelloAPI.delete_trello_board(TrelloBase.board_id)

@pytest.fixture(scope='module')
def driver():
    driver = webdriver.Firefox() 
    yield driver

def test_task_journey(driver, test_app):
    driver.get('http://localhost:5000')
    assert driver.title == 'To-Do App'

#def test_create_new_item(driver, test_app):
#    test_app


#def test_doing_item(driver, test_app):

#def test_done_item(driver, test_app): 

#def test_undo_item(driver, test_app):






