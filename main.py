import json

class JSONObjectTracker:
    def __init__(self):
        self.json_objects = {}

    def add_json_object(self, key, json_data):
        """
        Add a JSON object to the tracker.

        Parameters:
        - key (str): The key associated with the JSON object.
        - json_data (dict): The JSON object to be added.
        """
        if key in self.json_objects:
            print(f"Warning: Key '{key}' already exists. Overwriting the existing JSON object.")
        self.json_objects[key] = json_data
        print(f"JSON object with key '{key}' added successfully.")

    def get_json_object(self, key):
        """
        Retrieve a JSON object by its key.

        Parameters:
        - key (str): The key associated with the desired JSON object.

        Returns:
        - dict: The JSON object associated with the given key.
        """
        if key in self.json_objects:
            return self.json_objects[key]
        else:
            print(f"Error: JSON object with key '{key}' not found.")
            return None

# Example usage:
json_tracker = JSONObjectTracker()

# Adding JSON objects
json_data1 = {"name": "document1", "content": "This is the content of document 1.", "tags": ["tag1", "tag2"], "type": "text"}
json_tracker.add_json_object("doc1", json_data1)

json_data2 = {"name": "document2", "content": "This is the content of document 2.", "tags": ["tag1", "tag2"], "type": "text"}
json_tracker.add_json_object("doc2", json_data2)

# Retrieving JSON objects
retrieved_json1 = json_tracker.get_json_object("doc1")
if retrieved_json1:
    print("Retrieved JSON object 1:", retrieved_json1)

retrieved_json2 = json_tracker.get_json_object("doc2")  # Non-existing key
if retrieved_json2:
    print("Retrieved JSON object 2:", retrieved_json2)