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
    os.environ['TRELLO_BOARD_ID']  = TrelloAPI.create_trello_board("E2E test Board")

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

#@pytest.fixture(scope='module')
#def driver():
#    with webdriver.Firefox() as driver:
#        yield driver#
        
@pytest.fixture(scope='module')
def driver():
    opts = webdriver.ChromeOptions()
    opts.add_argument('--headless')
    opts.add_argument('--no-sandbox')
    opts.add_argument('--disable-dev-shm-usage')
    with webdriver.Chrome('./chromedriver', options=opts) as driver:
        yield driver        

def test_task_journey(driver, test_app):
    new_todo_item = "e2e todo item"
    driver.get('http://localhost:5000')
    
    assert driver.title == 'To-Do App'
    element = driver.find_element_by_id("add_todo_text_box")
    
    element.send_keys(new_todo_item)
    driver.find_element_by_id("add_todo_button").click()

    # Check new to do item has appeared.
    xpath = "//*[@id='ToDo']//*[@class='card_container']//*[@class='card_text' and text()='"+new_todo_item+"']"
    new_to_do = driver.find_element_by_xpath("//*[@id='ToDo']//*[@class='card_container']//*[@class='card_text' and text()='"+new_todo_item+"']")
    
    # Now click the button for the item
    move_to_doing_button = driver.find_element_by_xpath("//*[@id='ToDo']//*[@class='card_container']//*[@class='card_text' and text()='"+new_todo_item+"']/following-sibling::div/a/button")
    move_to_doing_button.click()

    # See if item now appears in Doing List
    new_doing_item = driver.find_element_by_xpath("//*[@id='Doing']//*[@class='card_container']//*[@class='card_text' and text()='"+new_todo_item+"']")

    # Now click the button for the item to moove to done
    move_to_done_button = driver.find_element_by_xpath("//*[@id='Doing']//*[@class='card_container']//*[@class='card_text' and text()='"+new_todo_item+"']/following-sibling::div/a/button")
    move_to_done_button.click()

    # See if item now appears in Done List
    new_done_item = driver.find_element_by_xpath("//*[@id='Done']//*[@class='card_container']//*[@class='card_text' and text()='"+new_todo_item+"']")



