
def boolean(x,a):

    if (x in a):
        return True
    return False


import random
a = random.sample(range(100), 10)
a.sort()
print(a)
print(boolean(10,a))