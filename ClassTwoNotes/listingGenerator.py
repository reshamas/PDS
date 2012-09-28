import listing
import random
import string

for i in range(50000):
    title_size = random.randrange(10, 180)
    title = ''.join(random.choice(string.ascii_uppercase + "        ") for x in range(title_size))

    description_size = random.randrange(50, 250)
    description = ''.join(random.choice(string.ascii_uppercase + "        ") for x in range(description_size))

    price = random.lognormvariate(4, .5)

    list = listing.Listing(1+i, title, description, price)
    print list.toJson()
