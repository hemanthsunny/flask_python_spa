import os
from pymongo import MongoClient

COLLECTION_NAME = 'kudos'
MONGO_URL="mongodb://mongo_user:mongo_secret@0.0.0.0:27017/"

class MongoRepository(object):
    def __init__(self):
        mongoUrl = MONGO_URL
        self.db = MongoClient(mongoUrl).kudos

    def find_all(self, selector):
        return self.db.kudos.find(selector)

    def find(self, selector):
        return self.db.kudos.find_one(selector)

    def create(self, selector):
        return self.db.kudos.replace_one(selector, kudo).modified_content

    def delete(self, selector):
        return self.db.kudos.delete_one(selector, kudo).delete_count

