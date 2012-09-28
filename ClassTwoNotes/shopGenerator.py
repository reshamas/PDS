import random
import string
import shop

listings = range(1,50000)
random.shuffle(listings)

users = range(1,10000)
random.shuffle(users)


for i in range(50000):
    if len(listings) == 0:
        break
    id = i+1
    name_size = random.randrange(10, 180)
    name = ''.join(random.choice(string.ascii_uppercase + "   ") for x in range(name_size))

    user = users.pop()

    s = shop.Shop(id, name, user)
    num_listings = int(round(random.lognormvariate(0, 5))) + 1 

    for j in range(num_listings):
        if len(listings) > 0:
            listing = listings.pop()
            count = int(round(random.lognormvariate(0, 5))) + 1

            s.addListing(listing, count)
    print s.toJson()
