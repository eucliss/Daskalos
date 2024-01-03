import pymongo

class MongoDBConnection:
    def __init__(self, host='localhost', port=27017):
        self.host = host
        self.port = port
        self.client = None

    def connect(self):
        try:
            self.client = pymongo.MongoClient(self.host, self.port)
            print("Connected to MongoDB")
        except pymongo.errors.ConnectionFailure as e:
            print(f"Could not connect to MongoDB: {e}")

    def close(self):
        if self.client:
            self.client.close()
            print("Connection to MongoDB closed")

    def get_database(self, db_name):
        if self.client:
            return self.client[db_name]
        else:
            raise Exception("MongoDB not connected")

    def get_collection(self, db_name, collection_name):
        if self.client:
            db = self.get_database(db_name)
            return db[collection_name]
        else:
            raise Exception("MongoDB not connected")

    def insert_document(self, db_name, collection_name, document):
        collection = self.get_collection(db_name, collection_name)
        result = collection.insert_one(document)
        return result.inserted_id

    def find_documents(self, db_name, collection_name, query=None):
        collection = self.get_collection(db_name, collection_name)
        if query:
            return collection.find(query)
        else:
            return collection.find()

    def update_document(self, db_name, collection_name, query, update_data):
        collection = self.get_collection(db_name, collection_name)
        result = collection.update_one(query, {"$set": update_data})
        return result.modified_count

    def delete_document(self, db_name, collection_name, query):
        collection = self.get_collection(db_name, collection_name)
        result = collection.delete_one(query)
        return result.deleted_count

# # Example usage:
# if __name__ == "__main__":
#     # Create a MongoDBConnection object
#     mongodb = MongoDBConnection()

#     # Connect to MongoDB
#     mongodb.connect()

#     # Access a database and a collection
#     db_name = "my_database"
#     collection_name = "my_collection"
#     db = mongodb.get_database(db_name)
#     collection = mongodb.get_collection(db_name, collection_name)

#     # Insert a document
#     document = {"name": "John", "age": 30}
#     inserted_id = mongodb.insert_document(db_name, collection_name, document)
#     print(f"Inserted document with ID: {inserted_id}")

#     # Find documents
#     documents = mongodb.find_documents(db_name, collection_name)
#     for doc in documents:
#         print(doc)

#     # Update a document
#     query = {"name": "John"}
#     update_data = {"age": 31}
#     modified_count = mongodb.update_document(db_name, collection_name, query, update_data)
#     print(f"Modified {modified_count} document(s)")

#     # Delete a document
#     delete_query = {"name": "John"}
#     deleted_count = mongodb.delete_document(db_name, collection_name, delete_query)
#     print(f"Deleted {deleted_count} document(s)")

#     # Close the MongoDB connection
#     mongodb.close()