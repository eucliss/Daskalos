from database import MongoDBConnection
import json

class NexusCore:
    
    def __init__(self, 
                 db_name='nexuscore', 
                 collection_name='test_collection',
                 tag_map='../tag_map.json',
                 word_map='../word_to_tag_map.json'):
        self.mongodb = MongoDBConnection()
        self.mongodb.connect()
        self.db_name = db_name
        # Collection name will be cs.AI or other categories
        self.collection_name = collection_name
        self.db = self.mongodb.get_database(db_name)
        self.collection = self.db.get_collection(collection_name)
        
        with open(tag_map) as f:
            self.tag_map = json.load(f)
        with open(word_map) as f:
            self.word_map = json.load(f)

    def disconnect(self):
        self.mongodb.close()

    def get_category_docs(self, category, count):
        collection = self.mongodb.get_collection('nexuscore', category)
        return collection.find().limit(count)

    def create_initial_document(self):
        return
        with open('../database.json') as f:
            data = json.load(f)
        categories = data.keys()
        for category in categories:
            print("Creating initial documents for category:", category)
            count = 0
            keys = data[category].keys()
            for key in keys:
                document = data[category][key]
                try:
                    pdf_id = document["id"].split('v')[0]
                except:
                    pdf_id = document["id"]
                document["pdf"] = f'https://arxiv.org/pdf/{pdf_id}.pdf'
                # self.db[category].insert_one(document)
                self.mongodb.insert_document(
                    self.db_name,
                    category,
                    document
                )
                count += 1
            # print("Initial documents created")
            print(self.mongodb.get_collection(self.db_name, category))
            print("--------------------")
            print(self.mongodb.get_collection(self.db_name, category).count_documents({}))

        

# nexus = NexusCore()
# nexus.create_initial_document()
# collection = nexus.mongodb.get_collection('nexuscore', 'cs.AI')
# documents = collection.find()
# for doc in nexus.get_collection_docs('cs.AI', 10):
#     print(doc)

# # Iterate through the documents and print each one
# for document in documents:
#     print(document)
# nexus.disconnect()