import random
random_numbers = []

for x in range(20):
    random_numbers.append(random.randint(0, 49))

squared_numbers = [num * num for num in random_numbers]
print(squared_numbers)