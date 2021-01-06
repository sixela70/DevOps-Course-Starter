class TrelloItem:

  def __init__(self, id, title, status):     
        self._id = id
        self._title = title
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
  def status(self):    
    return self._status

  @status.setter 
  def status(self,value):    
    self._status = value


