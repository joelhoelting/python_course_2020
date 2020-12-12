friend = "Rolf"
friends = ["Rolf", "Hilary", "Apples"]
family = ["Jenna", "Michael", "Debbie"]
username = input("Enter your name: ")

if username in friends:
    print("You are one of my friends")
elif username in family:
    print("You are my family")
else:
    print("I don't know you")
