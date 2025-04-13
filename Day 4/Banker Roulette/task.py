import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#Option 1
print(random.choice(friends))

#Option 2
chosen_number = random.randint(0,4)
print(f"Today {friends[chosen_number]} will be paying the bill")

