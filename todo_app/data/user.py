from flask_login import UserMixin

class User(UserMixin):
    
    readerRole = "ReaderRole"
    writerRole = "WriterRole"

    def __init__(self, id, username, role):
        self.id = id
        self.role = role
        self.username = username

    def is_readonly(self):
        return self.role == self.readerRole

    def __repr__(self):
        return '<User{} with Role{}>'.format(self.username, self.role)
