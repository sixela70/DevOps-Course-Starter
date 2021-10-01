from datetime import date, datetime

class Item:
  
  def __init__(self, id, title, status, dateLastActivity):     
        self._id = id
        self._title = title
        self._status = status
        self._dateLastActivity = dateLastActivity

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
  def dateLastActivity(self) -> datetime:     
    return self._dateLastActivity

  @dateLastActivity.setter 
  def status(self,value):    
    self._dateLastActivity = value

  @property 
  def status(self):    
    return self._status

  @status.setter 
  def status(self,value):    
    self._status = value

  def getItemAsJson(self):
    item =  { "id" : self.id,
              "title": self.title, 
             "status": self.status,
             "modified_date": self._dateLastActivity }
    return item

  @classmethod
  def isToDo(cls, item):
    if item.status == "ToDo":
        return True
    return False
 
  @classmethod
  def isDone(cls, item):
    if item.status == "Done":
        return True
    return False

  @classmethod
  def isDoing(cls, item):  
    if item.status == "Doing":
        return True
    return False

  @classmethod
  def isDoneToday(cls, item):
    date_today = datetime.today().date()
    if item.status == "Done":
      if item.dateLastActivity.date() == date_today:
        return True
    return False        

  @classmethod    
  def wasDoneBeforeToday(cls, item):
    date_today = datetime.today().date()
    if item.status == "Done":
      if item.dateLastActivity.date() < date_today:
        return True
    return False    

  @property 
  def info(self):
    return str(self.id)+','+self.title+','+self.status+','+str(self.dateLastActivity)









