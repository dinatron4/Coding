import random

# flag_head = 0
# flag_tails = 0

# for i in range(0,100):
#     number = random.randint(0,1)
#     if number == 0:
#         print("Head")
#         flag_head += 1
#     else:
#         print("Tails")
#         flag_tails += 1

# print(f"Heads: {flag_head}")
# print(f"Tails: {flag_tails}")

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(friends[random.randint(0,4)])
print(random.choice(friends))