friends = ["Rolf", "Jose", "Amanda", "Randy", "Rami"]

# friends_lower = map(lambda x: x.lower(), friends)
# friends_lower = [friend.lower() for friend in friends]
friends_lower = (friend.lower() for friend in friends)
print(friends_lower)
print(next(friends_lower))
print(list(friends_lower))


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def from_dict(cls, data):
        return cls(data['username'], data['password'])


user_list = [
    {'username': 'rolf', 'password': '123'},
    {'username': 'tecladoisawesome', 'password': 'youaretoo'}
]

users_one = [User.from_dict(user) for user in user_list]
users_two = map(User.from_dict, user_list)
print(list(users_one))
print(list(users_two))
