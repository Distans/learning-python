# listing human needs

security = 0
variety = 0
importance = 0
love = 0
growth = 0
contribution = 0

# defining print function


def get_results():
    print("Security: ", security)
    print("Variety: ", variety)
    print("Importance: ", importance)
    print("Love: ", love)
    print("Growth: ", growth)
    print("Contribution: ", contribution)


# comparing security and variety

print("What is more important to you?\n1: Security\n2: Variety")
result = input()
if result == '1':
    security += 1
elif result == '2':
    variety += 1
else:
    print("Please enter 1 or 2")

get_results()

# comparing security and importance

print("What is more important to you?\n1: Security\n2: Importance")
result = input()
if result == '1':
    security += 1
elif result == '2':
    importance += 1
else:
    print("Please enter 1 or 2")

get_results()

# comparing security and love

print("What is more important to you?\n1: Security\n2: Love")
result = input()
if result == '1':
    security += 1
elif result == '2':
    love += 1
else:
    print("Please enter 1 or 2")

get_results()

# comparing security and growth

print("What is more important to you?\n1: Security\n2: Growth")
result = input()
if result == '1':
    security += 1
elif result == '2':
    growth += 1
else:
    print("Please enter 1 or 2")

get_results()

# comparing security and contribution

print("What is more important to you?\n1: Security\n2: Contribution")
result = input()
if result == '1':
    security += 1
elif result == '2':
    contribution += 1
else:
    print("Please enter 1 or 2")

get_results()

# comparing variety and importance

print("What is more important to you?\n1: Variety\n2: Importance")
result = input()
if result == '1':
    variety += 1
elif result == '2':
    importance += 1
else:
    print("Please enter 1 or 2")

get_results()

# comparing variety and love

print("What is more important to you?\n1: Variety\n2: Love")
result = input()
if result == '1':
    variety += 1
elif result == '2':
    love += 1
else:
    print("Please enter 1 or 2")

get_results()

# comparing variety and growth

print("What is more important to you?\n1: Variety\n2: Growth")
result = input()
if result == '1':
    variety += 1
elif result == '2':
    growth += 1
else:
    print("Please enter 1 or 2")

get_results()

# comparing variety and contribution

print("What is more important to you?\n1: Variety\n2: Contribution")
result = input()
if result == '1':
    variety += 1
elif result == '2':
    contribution += 1
else:
    print("Please enter 1 or 2")

get_results()

# comparing importance and love

print("What is more important to you?\n1: Importance\n2: Love")
result = input()
if result == '1':
    importance += 1
elif result == '2':
    love += 1
else:
    print("Please enter 1 or 2")

get_results()

# comparing importance and growth

print("What is more important to you?\n1: Importance\n2: Growth")
result = input()
if result == '1':
    importance += 1
elif result == '2':
    growth += 1
else:
    print("Please enter 1 or 2")

get_results()

# comparing importance and contribution

print("What is more important to you?\n1: Importance\n2: Contribution")
result = input()
if result == '1':
    importance += 1
elif result == '2':
    contribution += 1
else:
    print("Please enter 1 or 2")

get_results()

# comparing love and growth

print("What is more important to you?\n1: Love\n2: Growth")
result = input()
if result == '1':
    love += 1
elif result == '2':
    growth += 1
else:
    print("Please enter 1 or 2")

get_results()

# comparing love and contribution

print("What is more important to you?\n1: Love\n2: Contribution")
result = input()
if result == '1':
    love += 1
elif result == '2':
    contribution += 1
else:
    print("Please enter 1 or 2")

get_results()

# comparing growth and contribution

print("What is more important to you?\n1: Growth\n2: Contribution")
result = input()
if result == '1':
    growth += 1
elif result == '2':
    contribution += 1
else:
    print("Please enter 1 or 2")

# printing final results

print("Your final results are:")
get_results()

