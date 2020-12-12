is_learning = True
counter = 0

while is_learning:
    print("You're Learning")
    user_input = input("ARe you still learning?: ");
    is_learning = user_input == "yes"
