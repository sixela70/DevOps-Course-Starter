
import requests
#import board
#from board import TrelloBoard
import json


# ToDo Board 
# Board consists of Lists
# Each list has a card 

Developer_API_key="2bf28cd9609b6d82c6accd4fa78be70c"
My_Secret="526dac3e066c92f0e02701bf983246e6a0aea2b065f516055e0f7e5098700caf"
Server_Token="94027d7e2a6eedb95e62a24826ae1eff2d074717a7db7e1c0b108210813c3cfa"
Base_Address="https://api.trello.com/1/members/me/"

response=requests.get('https://api.trello.com/1/members/me/boards?fields=name,id,url&key='+Developer_API_key+'&token='+Server_Token)
#print("CONTENT")
#print(response.content)
#print("TEXT")
#print(response.text)
#print("JSON")
jsonResponse = response.json()
print(jsonResponse[0])
#js = json.loads(jsonResponse[0])

print("Print each key-value pair from JSON response")
for key, value in jsonResponse[0].items():
    print(key, ":", value)

boardid=jsonResponse[0]['id']
print('Ssss')
print(boardid)
print('Ssss')

#https://api.trello.com/1/boards/{id}/cards?key=0471642aefef5fa1fa76530ce1ba4c85&token=9eb76d9a9d02b8dd40c2f3e5df18556c831d4d1fadbe2c45f8310e6c93b5c548

response=requests.get('https://api.trello.com/1/boards/'+boardid+'/cards?key='+Developer_API_key+'&token='+Server_Token)
print(response)
#print("CONTENT")
#print(response.content)
#print("TEXT")
#print(response.text)
#print("JSON")
jsonResponse = response.json()
print(len(jsonResponse))
print(jsonResponse)
print("Print each key-value pair from JSON response")
for item in jsonResponse:
    print(item['name']+item['id'])
#    for key, value in item.items():
#        print(key, ":", value)


#This givees the list of cards 

#GET /1/boards/{id}/lists

print('GET LISTS')

response=requests.get('https://api.trello.com/1/boards/'+boardid+'/lists?key='+Developer_API_key+'&token='+Server_Token)
print(response)
#print("CONTENT")
#print(response.content)
#print("TEXT")
#print(response.text)
#print("JSON")
jsonResponse = response.json()
print(len(jsonResponse))
print(jsonResponse)
print("Print each key-value pair from JSON response")
for item in jsonResponse:
    print(item['name']+item['id'])


#Doing5fbbf60323ecae55c9f1e78e
#DoneList5fbbf60323ecae55c9f1e78f
#ToDoList5fbbf61174585a44ac8bbccf


print('GET A LIST')

"https://api.trello.com/1/lists/{id}"
response=requests.get('https://api.trello.com/1/lists/5fbbf61174585a44ac8bbccf/cards?key='+Developer_API_key+'&token='+Server_Token)
print(response)
print("CONTENT")
print(response.content)
print("TEXT")
print(response.text)
print("JSON")
jsonResponse = response.json()
print(len(jsonResponse))
print(jsonResponse)
print("Print each key-value pair from JSON response")
for item in jsonResponse:
    print(item['name']+item['id'])












  # --url 'https://api.trello.com/1/cards?key=0471642aefef5fa1fa76530ce1ba4c85&token=9eb76d9a9d02b8dd40c2f3e5df18556c831d4d1fadbe2c45f8310e6c93b5c548&idList=5abbe4b7ddc1b351ef961414'
#def create_new_to_do_card( cardid) 



def create_card(list_id, card_name):
    url = "https://api.trello.com/1/cards"
    querystring = {"name": card_name, "idList": list_id, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring)
    card_id = response.json()["id"]
    return card_id






#Get all lists on a board 



#fetch_all_to_do_cards_from_board









"""

import requests
key = Developer_API_key
token = Server_Token
board_name = "banana4"
#def create_board(board_name):
url = "https://api.trello.com/1/boards"
querystring = {"name": board_name, "key": key, "token": token}
response = requests.request("POST", url, params=querystring)
board_id = response.json()["shortUrl"].split("/")[-1].strip()
print( board_id)



def create_card(list_id, card_name):
    url = f"https://api.trello.com/1/cards"
    querystring = {"name": card_name, "idList": list_id, "key": key, "token": token}
    response = requests.request("POST", url, params=querystring)
    card_id = response.json()["id"]
    return card_id
"""

#response=requests.post('https://api.trello.com/1/members/me/boards?key='+Developer_API_key+'&token='+Server_Token)
#print(response)

#board_id = response.json()["shortUrl"].split("/")[-1].strip()
#print(board_id)

"""
import requests
key = "your_key"
token = "your_token"
def create_board(board_name):
    url = "https://api.trello.com/1/boards/"
    querystring = {"name": board_name, "key": Developer_API_key, "token": Server_Token}
    response = requests.request("POST", url, params=querystring)
    board_id = response.json()["shortUrl"].split("/")[-1].strip()
    return board_id

print(r)
js = json.loads(r.text)
# js1 = json.loads(js[0])
print(type(js))

print(len(js))
for item in js:
    print(item)
    print('banana')
#print(my_json_response)

print(js['name'])
#my_json_response.
#name=data['name']
#desc=data['desc']
#id=data['id']

#board = TrelloBoard.populate(my_json_response)

#print ( board.name)




#create_new_to_do_card

#move_card_from_to_do_to_done 
"""