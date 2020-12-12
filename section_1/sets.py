# art_friends = {"Rolf", "Anne", "Jenn"}
# science_friends = {"Jenn", "Charlie"}
#
# # art_friends.add("Jenn")
# # print(art_friends)
# # art_friends.remove("Rolf")
# # print(art_friends)
#
# art_but_not_science = art_friends.difference(science_friends)
# science_but_not_art = science_friends.difference(art_friends)
#
# # Everyone but "Jenn"
# not_in_both = art_friends.symmetric_difference(science_friends)
#
# # Get member in both sets
# art_and_science = art_friends.intersection(science_friends)
#
# # Unite sets
# all_friends = art_friends.union(science_friends)
# print(all_friends)

nearby_people = {'Rolf', 'Jen', 'Anna'}
user_friends = set()  # This is an empty set, like {}

# Ask the user for the name of a friend
new_friend = input("Please give name of friend: ")
user_friends.add(new_friend)

intersected_friends = nearby_people.intersection(user_friends)
print(intersected_friends)