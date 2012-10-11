# Now for the recommender system part of the Class 2 Lab exercise
#  This is Foster's code...
#  This is from the second recitation -- Monday Oct 8, 2012
#  We will now look at question #3

import User
import Listing
import Shop

# The reading in of the data is just cut-and-paste from the prior
# recitation code (in data_analysis_reco.py) -- for the first 2
# questions of the Class 2 lab exercise

# Get the users, listings, and shops from the data files

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

### We don't really need these right now, so let's comment them out
# all_listings=[]
# 
# for line in listing_file:
#     new_listing = Listing.fromJson(line)
#     all_listings.append(new_listing)
# listing_file.close()
# 
# print len(all_listings)
# 
# all_shops=[]
# 
# for line in shop_file:
#     new_shop = Shop.fromJson(line)
#     all_shops.append(new_shop)
# shop_file.close()
# 
# print len(all_shops)
# 
##########  data are read in ######
### the new stuff in this lab session is below here ####

#In the lab we spent a lot of time taking small steps toward our goal,
# under the philosophy: make sure you can do each piece, both to build
# confidence and also to focus in on exactly where the error is, when it
# inevitably comes.  I've not included all those little steps here, but
# here might be a first one:

# If I need to collect as recommendations all the favorites of each user's friends
#  I might start by just seeing if I can at least get the first user's friends:

print "Look at User index 20's friends:"
print all_users[20].friends

# Now, we're going to want to find the friends' favorites.  That means
#  we need to be able to get the class object for an arbitrary friend.
#  Looking at the friends of user0, we see that they are represented
#  by user.id We could make some assumptions about the users being
#  stored in order in the file by id, but I'd much rather not have my
#  analysis depend on such an assumption.  It's easier to just build a
#  lookup table that finds the user I want given her id:

#Make a lookup table for users by their ids, so we can find a certain
#user when we need to
user_lookup = dict()
for u in all_users:
    user_lookup[u.id]=u 

#Check that that worked, plus
#For a sanity check at the end, check the recommendations for User 20...
print "User id 20's friends: ", user_lookup[20].friends
print "User 321's favs: ", user_lookup[321].favorites
print "User 4032's favs: ", user_lookup[4032].favorites


###
#Now, collect the favorites for all the friends of each of the users:

# this would initialize a list of empty sets.  We don't need it though.
# friends_favorites = [set() for x in range(len(all_users)+1)]
# I found a code snippet like that on stackoverflow for initializing a list
# here I modified it to have a list of empty friend sets for the users

friends_favorites= dict() # each entry will be the set of all friends' favs
for u in all_users:
    #print u, u.id
    friends_favorites[u.id] = set() # initialize to empty set
    for f_id in u.friends:
        afriend = user_lookup[f_id]
        #print "Friend and favorites: ",f_id, afriend.favorites
        friends_favorites[u.id] |= afriend.favorites

print "User and friends favorites: ", 20, friends_favorites[20]
# that was just to check to see if it was working, in combo with the print
# statements in the for loop above

###
#Now store the recommendations for each user

#I think I'll try to save them in json, but just do it manually:
#  (see examples in Class 2 document on json):

# I'm also going to try to use formatted printing (see LPTHW)

reco_filename = "ecommerce/recos.json"
reco_file = open(reco_filename, 'w')

print "Recommendations printing to ", reco_filename
for u in all_users:
    #print "{\"id\":%s, \"recommendations\":%s}\n" % (u.id, list(friends_favorites[u.id]))
    line =  "{\"id\":%s, \"recommendations\":%s}\n" % (u.id, list(friends_favorites[u.id]))
    reco_file.write(line)

reco_file.close()


