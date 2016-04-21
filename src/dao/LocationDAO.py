from src.db.DbHelper import DbHelper


class LocationDAO:
   __db = None;

   def __init__(self):
       self.__db = DbHelper()

   def getLocations(self):
       return self.__db.query("SELECT * FROM locations", None).fetchall();