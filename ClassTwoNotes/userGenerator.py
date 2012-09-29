import random
from uuid import uuid4
from user import User
import json

for j in range(10000):
    id = j+1 #incremental user ids
    name = str(uuid4()) #make up a random user name
    email = "xxx@yyy.com" #dummy user ids
    #randomly assign gender   
    u = User(id, name, email, random.choice(["male", "female", "private", ""]))


    d = 4*random.random()
    #a long-tailed number of favorites
    num_favorites = int(round(random.lognormvariate(d, .5)))%1000

    for i in range(num_favorites):
        #the actual favorites are also drawn from a long tail
        fav_id = 0
        while True:            
            fav_id = (1+int(round(random.lognormvariate(4, 5))))%50000 
            if fav_id != 0:
                break
        u.addFavorite(fav_id)
        
    #a long-tailed number of friends

    num_friends = int(round(random.lognormvariate(d, .5)))

    for i in range(num_friends):
        #long-tailed distribution on friends
        friend_id = 0
        while True:
            friend_id = (1+int(round(random.lognormvariate(4, 5))))%10000
            if friend_id != 0:
                break
        u.addFriend(friend_id)

    #long-tailed number of purchases
    num_purchases = int(round(random.lognormvariate(d/2, .1))) - 2

    for i in range(num_purchases):
        pruch_id = 0
        while True:
            purch_id = (1+int(round(random.lognormvariate(4, 4.5))))%50000
            if purch_id != 0:
                break
        u.addPurchase(purch_id)

    
    #print "%d\t%d\t%d\t%d" %(u.id, len(u.favorites), len(u.friends), len(u.purchases))

    print u.toJson()
