def starts_with_r(friend):
    return friend.startswith('R')


friends = ["Rolf", "Jose", "Amanda", "Randy", "Rami"]
start_with_r = filter(starts_with_r, friends)  # arg1: function that returns true or false
# start_with_r = my_custom_filter(lambda friend: friend.startswith("R"),
#                                 friends)  # arg1: function that returns true or false
another_starts_with_r = (f for f in friends if f.startswith(('R')))


# print(next(start_with_r))
# print(next(start_with_r))
# print(next(start_with_r))

# print(list(start_with_r))
# print(list(another_starts_with_r))

def my_custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i


start_with_r = my_custom_filter(lambda friend: friend.startswith("R"), friends)
print(next(start_with_r))
print(next(start_with_r))
print(next(start_with_r))
