import json

class Shop:
    def __init__(self, id, name, user, listings = dict()):
        self.id = id
        self.name = name
        self.user = user
        self.listings = listings

    def addListing(self, listing, quantity = 1):
        self.listings[listing] = self.listings[listing] + quantity if self.listings.has_key(listing) else quantity

    def getQuantity(self, listing):
        return self.listings[listing] if self.listings.has_key(listing) else 0

    def toJson(self):
        return json.dumps(self.__dict__)

def fromJson(json_string):
    json_map = json.loads(json_string)
    return Shop(json_map["id"], json_map["name"], json_map["listings"])
