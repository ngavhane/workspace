from flask_pymongo import PyMongo
from pymongo import MongoClient

def connect():
# Substitute the 5 pieces of information you got when creating
# the Mongo DB Database (underlined in red in the screenshots)
# Obviously, do not store your password as plaintext in practice
    connection = MongoClient("ds117913.mlab.com",17913)
    handle = connection["acr"]
    handle.authenticate("niteengavhane4p","Boysarebest@1")
    return handle
