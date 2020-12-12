friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

# Instead of this
long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))
    if time_since_seen[i] > 5
}

# Use zip to simplify
print(list(zip(friends, time_since_seen, [1, 2, 3, 4])))

