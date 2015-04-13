# your code goes here
# make an empty dictionary
# Open the file
# format it so that it's readable
# for each line:
#    make a key-value pair in the dictionary of restaurant name:rating
# output should be chained, sorted key:value for each iteration

restaurant_ratings = {}

rating_info = open("scores.txt")

for line in rating_info:
    name, rating = line.rstrip().split(":")
    restaurant_ratings[name] = rating

sorted_names = sorted(restaurant_ratings)

for name in sorted_names:
    print "Restaurant", name, "is rated at", restaurant_ratings[name]

