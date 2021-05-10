class TrelloItem:

  def __init__(self, id, title, status):     
        self._id = id
        self._title = title
        self._status = status
        print(dateLastActivity)


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
  def status(self):    
  #  if self.status == None: Why this gives me a recursive error I would like to know I must bne being a **&
  #    return "None"
    return self._status

  @status.setter 
  def status(self,value):    
    self._status = value

<<<<<<< HEAD
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

  @classmethod
  def isDoneToday(cls, trello_item):
    date_today = datetime.today().date()
    if trello_item.idList == TrelloBase.get_done_list_id():
      if trello_item.dateLastActivity.date() == date_today:
        return True
    return False        

  @classmethod    
  def wasDoneBeforeToday(cls, trello_item):
    date_today = datetime.today().date()
    if trello_item.idList == TrelloBase.get_done_list_id():
      if trello_item.dateLastActivity.date() < date_today:
        return True
    return False    
    
  @property 
  def info(self):
    return str(self.id)+','+self.title+','+str(self.idList)+','+str(self.dateLastActivity)#+","+self.status








=======
>>>>>>> parent of 1cf02dc (Merge from exercise-3)

