# Now for the starred question in the recommender system part of the Class 2 Lab exercise
#  This is Foster's code...
#   (Class 2 Lab exercise, Question 4)

#see the comments for all this in the files for the prior questions
# I deleted extraneous stuff here.

import User
import sys

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
user_file.close()
print len(all_users)

##########  data are read in ######
### the new stuff in this lab session is below here ####

### main reco code is in reco.py

###
#Now, let's think about the starred question.  I'm going to try to
# redo the analysis, but now I'll order each user's recommendations by
# how many times their friends have favorited them.  I"m just going to
# try to update the prior code, from reco.py.

print "Look at User 19's friends:"
print all_users[19-1].friends

#Make a lookup table for users by their ids, so we can find a certain
#user when we need to
user_lookup = dict()
for u in all_users:
    user_lookup[u.id]=u

    #print user_lookup[19].friends

###
#Now, collect the favorites for all the friends of each of the users:

# This time I will make each user's friends' favorites a dict.  The keys will
# be the favorites, and then the value will be the number of times it
# was favorited (if any).

# so the larger collection (friends_favorites) will be a dict of dicts

all_users_friends_favorites = dict() # indexed by id

for u in all_users:
    #print "User: ", u.id
    all_users_friends_favorites[u.id]=dict()
    for f_id in u.friends:
        #print "Friend: ", f_id
        this_friend = user_lookup[f_id]
        for favorite in list(this_friend.favorites):
            #tally number of times favorited by different friends
            if not all_users_friends_favorites[u.id].has_key(favorite):
                all_users_friends_favorites[u.id][favorite] = 1
            else:
                all_users_friends_favorites[u.id][favorite] += 1

who=1
print "User and friends favorites: ", who , all_users_friends_favorites[who]
print "User and friends favorites: ", 2, user_lookup[2].favorites
# that was just to check to see if it was working, in combo with the print
# statements in the for loop above

###
#Now we have to *sort* the recommendations by the number of friends favorites

#On stackoverflow (after googling) there were a bunch of ways to do
#that.  Here's one: sorted(d.items(), key=lambda x: x[1])

# (I chose this one because I used to use lambda functions >two
# decades ago in Lisp -- a functional programming language -- and this
# seemed like an opportunity to figure out what they were in Python.
# From this: http://www.secnetix.de/olli/Python/lambda_functions.hawk
#  I kind of get it, but I lost interest pretty quickly.)

recos = dict() # this will store the final recommendations, indexed by user id
for u in all_users:
    reco_sorted = sorted(all_users_friends_favorites[u.id].items(), key=lambda x: -x[1])
    # that contains a sorted list of (favorite, tally) pairs
    # we just want the sorted list of favorites
    # NOTE: I developed this through the same step-by-step process we've gone over
    #  in the recitations: I saw that I could generate those sorted pairs, and then
    #  that generated a task for me to get the first elements of the pairs out.
    recos[u.id]=list() # this will contain user u.id's sorted recos (the favs only)
    for reco in reco_sorted:
        #print reco
        recos[u.id].append(reco[0]) # get just the first element
        #print "Recos: ", u.id, recos[u.id]
        # Uncomment those print statements and watch it work.
        # HINT: when you run your program on unix you can pipe it into
        # "more" so the output doesn't just whip by.
        # like this:
        # python starred_reco.py | more

who = 1
print "\nUser %s's recos: %s" % (who, recos[who])

#sys.exit()

###
#Now store the recommendations for each user

#I think I'll try to save them in json, but just do it manually:
#  (see examples in Class 2 document on json):

# I'm also going to try to use formatted printing (see LPTHW)

reco_filename = "ecommerce/recos_ordered.json"
reco_file = open(reco_filename, 'w')

for u in all_users:
    #print "{\"id\":%s, \"recommendations\":%s}" % (u.id, recos[u.id])
    line =  "{\"id\":%s, \"recommendations\":%s}\n" % (u.id, recos[u.id])
    reco_file.write(line)
print "\nRecommendations should be stored in ", reco_filename
reco_file.close()

