import json

class Listing:
    def __init__(self, id, title, description, price):
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        
    def toJson(self):
        return json.dumps(self.__dict__)

def fromJson(json_string):
    json_map = json.loads(json_string)
    return Listing(json_map["id"], json_map["title"], json_map["description"], json_map["price"])
