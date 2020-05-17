import random

a = random.sample(range(100), 20)
b = random.sample(range(100), 20)
c = [x for x in a if x in b]

print(c)