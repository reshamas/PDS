

class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.gender = "N/A"
        self.favorites = []
        self.purchases = []
        self.friends = set()

    def addFavorite(self, favorite):
        self.favorites.append(favorite)

    def addPurchase(self, item):
        self.purchases(item)

    def addFriend(self, friend):
        self.friends.add(friend)
