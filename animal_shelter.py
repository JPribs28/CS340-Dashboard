from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """


    # Init and connect to database with credentials
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:37706/AAC' % (username, password))
        self.database = self.client.AAC	
        self.collection = self.database.animals


    # Returns True is new entry is successfully added, in not will return False.
    def create(self, data):

        if self.collection.insert(data): # data should be dictionary 
            return True             
        return False
        

    # Retrieve documents from the 'animals' collection and returned as a list.
    def read(self, query):
        return self.collection.find(query, {"_id":False})


    # Updates a document from the 'animals' collection and returns JSON updated document    
    def update(self, query, data):
        return self.collection.update(query, {'$set': data})


    # Deletes a document from the 'animals' collection
    def delete(self, query):
        return self.collection.remove(query)
