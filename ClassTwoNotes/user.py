import json

class User:
    def __init__(self, id, name, email, gender = "", favorites = set(), purchases = [], friends = set()):
        self.id = id
        self.name = name
        self.email = email
        self.gender = gender
        self.favorites = favorites
        self.purchases = purchases
        self.friends = friends

    def addFavorite(self, favorite):
        self.favorites.add(favorite)

    def addPurchase(self, item):
        self.purchases.append(item)

    def addFriend(self, friend):
        self.friends.add(friend)

    def toJson(self):
        return json.dumps(self.__dict__, cls=SetEncoder)

class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder(self, obj)


def fromJson(json_string):
    json_map = json.loads(json_string)
    return User(json_map["id"], json_map["name"], json_map["email"], set(json_map["favorites"]), json_map["purchases"], set(json_map["friends"]))
