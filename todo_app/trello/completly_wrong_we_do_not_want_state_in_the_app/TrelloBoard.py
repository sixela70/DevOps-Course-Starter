"""
[
    {'name': 'My TODO', 'desc': '', 'descData': None, 'closed': False, 'idOrganization': '5fbbda89583ee2554b648de8', 'idEnterprise': None, 'limits': None, 'pinned': None, 'shortLink': '3BlObFTk', 'powerUps': [], 
    'dateLastActivity': '2020-11-23T17:49:19.026Z', 'idTags': [], 'datePluginDisable': None, 'creationMethod': 'automatic', 'ixUpdate': None, 'enterpriseOwned': False, 'idBoardSource': None, 
    'idMemberCreator': '5fb3ae30cecffc5b2a84f589', 'id': '5fbbf60323ecae55c9f1e78c', 'starred': False, 'url': 'https://trello.com/b/3BlObFTk/my-todo', 'prefs': {'permissionLevel': 'org', 'hideVotes': False, 'voting': 'disabled', 'comments': 'members', 'invitations': 'members', 'selfJoin': True, 'cardCovers': True, 'isTemplate': False, 'cardAging': 'regular', 'calendarFeedEnabled': False, 'background': '5fbbe723adbb940174e3ac23', 'backgroundImage': 'https://trello-backgrounds.s3.amazonaws.com/SharedBackground/original/0a13ae2e1a8aa91e0c9013a5c63683cf/photo-1606000759176-ac2814edc0a0', 'backgroundImageScaled': [{'width': 125, 'height': 100, 'url': 'https://trello-backgrounds.s3.amazonaws.com/SharedBackground/125x100/a62f4e922ebee45a17fa425cd9093b57/photo-1606000759176-ac2814edc0a0.jpg'}, {'width': 240, 'height': 192, 'url': 'https://trello-backgrounds.s3.amazonaws.com/SharedBackground/240x192/a62f4e922ebee45a17fa425cd9093b57/photo-1606000759176-ac2814edc0a0.jpg'}, {'width': 480, 'height': 384, 'url': 'https://trello-backgrounds.s3.amazonaws.com/SharedBackground/480x384/a62f4e922ebee45a17fa425cd9093b57/photo-1606000759176-ac2814edc0a0.jpg'}, {'width': 960, 'height': 768, 'url': 'https://trello-backgrounds.s3.amazonaws.com/SharedBackground/960x768/a62f4e922ebee45a17fa425cd9093b57/photo-1606000759176-ac2814edc0a0.jpg'}, {'width': 1024, 'height': 819, 'url': 'https://trello-backgrounds.s3.amazonaws.com/SharedBackground/1024x819/a62f4e922ebee45a17fa425cd9093b57/photo-1606000759176-ac2814edc0a0.jpg'}, {'width': 2048, 'height': 1638, 'url': 'https://trello-backgrounds.s3.amazonaws.com/SharedBackground/2048x1638/a62f4e922ebee45a17fa425cd9093b57/photo-1606000759176-ac2814edc0a0.jpg'}, {'width': 1280, 'height': 1024, 'url': 'https://trello-backgrounds.s3.amazonaws.com/SharedBackground/1280x1024/a62f4e922ebee45a17fa425cd9093b57/photo-1606000759176-ac2814edc0a0.jpg'}, {'width': 1920, 'height': 1535, 'url': 'https://trello-backgrounds.s3.amazonaws.com/SharedBackground/1920x1535/a62f4e922ebee45a17fa425cd9093b57/photo-1606000759176-ac2814edc0a0.jpg'}, {'width': 2001, 'height': 1600, 'url': 'https://trello-backgrounds.s3.amazonaws.com/SharedBackground/2001x1600/a62f4e922ebee45a17fa425cd9093b57/photo-1606000759176-ac2814edc0a0.jpg'}, {'width': 2560, 'height': 2047, 'url': 'https://trello-backgrounds.s3.amazonaws.com/SharedBackground/original/0a13ae2e1a8aa91e0c9013a5c63683cf/photo-1606000759176-ac2814edc0a0'}], 'backgroundTile': False, 'backgroundBrightness': 'dark', 'backgroundBottomColor': '#636c6b', 'backgroundTopColor': '#50696c', 'canBePublic': True, 'canBeEnterprise': True, 'canBeOrg': True, 'canBePrivate': True, 'canInvite': True}, 'subscribed': False, 'labelNames': {'green': '', 'yellow': '', 'orange': '', 'red': '', 'purple': '', 'blue': '', 'sky': '', 'lime': '', 'pink': '', 'black': ''}, 'dateLastView': '2020-11-23T17:54:20.075Z', 'shortUrl': 'https://trello.com/b/3BlObFTk', 'templateGallery': None, 'premiumFeatures': [], 'memberships': [{'id': '5fbbf60323ecae55c9f1e790', 'idMember': '5fb3ae30cecffc5b2a84f589', 'memberType': 'admin', 'unconfirmed': False, 'deactivated': False}]}]
"""

from typing import NamedTuple
from .TrelloBase import TrelloBase
from .TrelloList import TrelloList
import requests

# Trello Board holds its id and a list of the lists definied in the board
# I want the board when passed in its name to populate the hierarchy from trello cloud 

class TrelloBoard:

    branch_url = "boards/"

    def __init__(self, id, name, url): 
        self.name = name
        self.url = url
        self.id = id
        self.lists = []

    @classmethod
    def get_board_url(cls, filter):
        url = TrelloBase.base_address+TrelloBoard.branch_url+filter+TrelloBase.auth_tokens()
        print('Request URL :' + url)
        return url

    #Hardcode to go get my board for the exercise 
    @classmethod
    def get_my_board(cls):
        url = 'https://api.trello.com/1/members/me/boards?fields=name,id,url'+TrelloBase.auth_tokens()
        response= requests.get(url)
        jsonResponse = response.json()
        return TrelloBoard.populate(jsonResponse[0]['id'],jsonResponse[0]['name'],jsonResponse[0]['url'])   # Do not like this 

    @classmethod 
    def populate(cls, id,name,url):
        new_board = TrelloBoard(id,name,url)
        #Get the list of lists
        url = TrelloBoard.get_board_url(id+'/lists?') 
        response= requests.get(url)
        jsonResponse = response.json()        
        for item in jsonResponse:
            new_list = TrelloList.populate(item['id'],item['name'],id)
            new_board.lists.append(new_list)


    def GetDoingList():
        return None

    def GetDoneList():
        return None

    def GetToDoList():        
        return None






