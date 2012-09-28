import random
from uuid import uuid4
import user
import json

for i in range(10000):
    id = i+1 #incremental user ids
    name = str(uuid4()) #make up a random user name
    email = "xxx@yyy.com" #dummy user ids
   
    u = user.User(id, name, email, random.choice(["male", "female", "private", ""]))

    #a long-tailed number of favorites
    num_favorites = int(round(random.lognormvariate(2, 2.5)))

    for i in range(num_favorites):
        #the actual favorites are also drawn from a long tail
        fav_id = int(round(random.lognormvariate(4, 3)))%50000
        u.addFavorite(fav_id)
        
    #a long-tailed number of friends
    num_friends = int(round(random.lognormvariate(2, 2.5)))

    for i in range(num_friends):
        #long-tailed distribution on friends
        friend_id = int(round(random.lognormvariate(4, 2)))%10000
        u.addFriend(friend_id)

    #long-tailed number of purchases
    num_purchases = int(round(random.lognormvariate(0, 2)))

    for i in range(num_purchases):
        purch_id = int(round(random.lognormvariate(4, 3)))%50000
        u.addPurchase(purch_id)

    #randomly assign gender
    

    print u.toJson()
