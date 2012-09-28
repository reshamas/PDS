import json

class Shop:
    def __init__(self, id, name, listings = dict()):
        self.id = id
        self.name = name
        self.listings = listings

    def addListing(self, listing, quantity = 1):
        self.listings[listing] = self.listings[listing] + quantity if self.listings.has_key(listing) else quantity

    def getQuantity(self, listing):
        return self.listings[listing] if self.listings.has_key(listing) else 0

    def toJson(self):
        return json.dumps(self.__dict__)
