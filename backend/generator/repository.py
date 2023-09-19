from pymongo import MongoClient


class Repository:
    __instance = None

    @staticmethod
    def getInstance():
        """Static access method."""
        if Repository.__instance == None:
            Repository()
        return Repository.__instance

    def __init__(self):
        self.client = MongoClient("mongodb://root:password@localhost:27017/")
        """ Virtually private constructor. """
        if Repository.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Repository.__instance = self
