from src.db.DbHelper import DbHelper


class UserDAO(object):
   __db = None;

   def __init__(self):
       self.__db = DbHelper()

   def getUsers(self):
       return self.__db.query("SELECT * FROM users", None).fetchall();