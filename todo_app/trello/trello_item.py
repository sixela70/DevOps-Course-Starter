from todo_app.trello.trello_base import TrelloBase

class TrelloItem:

  def __init__(self, id, title, idList, status = None):     
        self._id = id
        self._title = title
        self._idList = idList
        self._status = status

  @property
  def id(self):
    return self._id

  @id.setter    
  def id(self,value):
    self._id = value

  @property 
  def title(self):
    return self._title

  @title.setter 
  def title(self,value):
     self._title = value

  @property 
  def idList(self):
    return self._idList

  @property 
  def status(self):    
    return self._status

  @status.setter 
  def status(self,value):    
    self._status = value

  @classmethod
  def isToDo(cls, trello_item):
    if trello_item.idList == TrelloBase.get_todo_list_id():
        return True
    return False

  @classmethod
  def isDone(cls, trello_item):
    if trello_item.idList == TrelloBase.get_done_list_id():
        return True
    return False

  @classmethod
  def isDoing(cls, trello_item):
    if trello_item.idList == TrelloBase.get_doing_list_id():
        return True
    return False







