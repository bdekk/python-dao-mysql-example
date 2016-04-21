from src.dao.UserDAO import UserDAO
from src.dao.LocationDAO import LocationDAO

__author__ = "Bram Dekker"

class App(object):
    def __init__(self):

        __udao = UserDAO()
        __ldao = LocationDAO();
        print(__udao.getUsers())
        print(__ldao.getLocations())
        # print();


if __name__ == "__main__":
    app = App();