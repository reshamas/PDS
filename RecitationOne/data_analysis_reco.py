### This is Foster's rough code solution to the PDS Class 2 Lab Exercise parts 1 & 2

### This is more-or-less a recreation of the Friday recitation --
### except that this may be more complete.

import User
import Listing
import Shop

import numpy as np
import matplotlib.pyplot as plt

# I imported the sys package after trying to figure out how to stop my program
# at arbitrarly places while I was developing it.  I found online that sys.exit()
# does what I want.
import sys

# The next section reads in the data.  These lines are what I typed in
# following Josh's on-screen coding in class -- not exactly the same,
# but functionally so.  Note that I tend to insert print statements
# everywhere, as I slowly build up my code.  I like to know each step
# of the way whether the code is actually doing what I think.  It's a
# little slower if I actually get everything right the first time.
# It's much faster since I usually don't get things right the first
# time.

user_filename= "ecommerce/users.json"
listing_filename = "ecommerce/listings.json"
shop_filename = "ecommerce/shops.json"

user_file = open(user_filename, 'r')
listing_file = open(listing_filename, 'r')
shop_file = open(shop_filename, 'r')

all_users=[]

for line in user_file:
    new_user = User.fromJson(line)
    all_users.append(new_user)
    #print line
    #print all_users[0].purchases
    #sys.exit()
user_file.close()

print len(all_users)

all_listings=[]

for line in listing_file:
    new_listing = Listing.fromJson(line)
    all_listings.append(new_listing)
listing_file.close()

print len(all_listings)

all_shops=[]

for line in shop_file:
    new_shop = Shop.fromJson(line)
    all_shops.append(new_shop)
shop_file.close()

print len(all_shops)

##########  data are read in ######

# Now I'm going to tally up how many users have 1 friend, 2 friends, 3
# ... etc., and the same for favs and purchases

num_friends = dict()  #each dict will key on the number (say, of friends)
num_favorites = dict() # and the entry will be the tally
num_purchases = dict()

# Now do the tallying
for u in all_users: # look at each user
    num_favorite = len(u.favorites) # figure out how many favs she has
    num_friend = len(u.friends)
    num_purchase = len(u.purchases)

    #    print u.purchases
    #    print num_purchase
    # sys.exit()

    # if you've never seen this number before, make tally one
    if not num_favorites.has_key(num_favorite): 
        num_favorites[num_favorite] = 1 
    else: #otherwise, increment the tally
        num_favorites[num_favorite] += 1

    if not num_friends.has_key(num_friend):
        num_friends[num_friend] = 1
    else:
        num_friends[num_friend] += 1

    if not num_purchases.has_key(num_purchase):
        num_purchases[num_purchase] = 1
    else:
        num_purchases[num_purchase] += 1

#Just to check: print out these dicts
print "Favorite tallies: ", num_favorites
print "Friend tallies: ", num_friends
print "Purchase tallies: ", num_purchases

#Now, I'm going to print the distributions as a bar chart.  For my
#HW#1 I had experimented a good bit with both histograms and bar
#charts.  I got a little further with making nice-looking bar charts,
#so I decided just to paste that code in here and adapt it to the
#present task.  (I'm hoping that as I build up a bunch of such
#visualizations, I can often just grab some code from a prior
#analysis.)

# My bar charting code needs the distributions explicitly represented
# in Python arrays (lists) rather than in dicts, so now I'm going to
# just do the transfer.  There may be a quick way to do this in
# Python, but I took the easy way out and just did the transfer with a
# loop.


# loop through the range of numbers of favorites (and then friends,
# purchases)

# note that some numbers of favs may not have gotten any tallies (!)
# so I'll explicitly run up through the maximum key value for each
favorite_dist=[]
for i in range(max(num_favorites.keys())+1): #add one because starts at zero
    #print i
    if not num_favorites.has_key(i):
        num_favorites[i] = 0
    favorite_dist.append(num_favorites[i])

print "Favorites: ", favorite_dist

friend_dist=[]
for i in range(max(num_friends.keys())+1):
    #print i
    if not num_friends.has_key(i):
        num_friends[i] = 0
    friend_dist.append(num_friends[i])

print "Friends: ", friend_dist

purchase_dist=[]
for i in range(max(num_purchases.keys())+1):
    #print i
    if not num_purchases.has_key(i):
        num_purchases[i] = 0
    purchase_dist.append(num_purchases[i])

print "Purchases: ", purchase_dist

#####Now print bar-chart histogram####

#When I first tried this, I got an error because the distributions were
#not all the same width, and the plotting function wanted them to be
#SO ... I made them all as long as the longest one:

print len(favorite_dist), len(friend_dist), len(purchase_dist)
N = max(len(favorite_dist), len(friend_dist), len(purchase_dist))

#sys.exit()  # stop here for now

#I found this little code snippet for padding the list with zeros on
#stackoverflow:
friend_dist = friend_dist +  [0 for _ in range(N-len(friend_dist))]
purchase_dist = purchase_dist +  [0 for _ in range(N-len(purchase_dist))]
favorite_dist = favorite_dist +  [0 for _ in range(N-len(favorite_dist))]

print N
print len(favorite_dist)
print len(friend_dist)
print len(purchase_dist)
#see -- they're all 198 long now

#sys.exit()

#N here controls how wide the bar charts actually are.  Making it 198
#shows the whole chart.  Making it smaller, zooms in on the left-hand
#portion -- and thereby shows the bars better.
N=30

#I got this code from the web and modified it:
ind = np.arange(N)  # we're going to have N groups of bars
                    # ind gives the indices of left-hand points on the x-axis
width = 0.7/3       # the width of the bars
                    # why 0.7?  I'll let you figure that out.

#Code modified pretty directly from what I found on the web:
plt.subplot(111)
rects1 = plt.bar(ind, favorite_dist[0:N], width,
                    color='r')

rects2 = plt.bar(ind+width, friend_dist[0:N], width,
                   color='y')
 
rects3 = plt.bar(ind+2*width, purchase_dist[0:N], width,
                    color='b')
 
# add some information
plt.ylabel('Counts')
plt.title('Counts of different User collections')
plt.legend( (rects1[0], rects2[0], rects3[0]), ('Favorites', 'Friends', 'Purchases') )

#I found this too.
#First I tried just "log"; I didn't like the
#result, so I searched on what bothered me about it and found "symlog"
plt.yscale('symlog')

plt.show()

#Q: How would you *save* your plot to a file?

