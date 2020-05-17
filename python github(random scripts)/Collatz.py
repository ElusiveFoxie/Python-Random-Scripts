
def Collatz(number):
    if (number % 2 == 0):
        return (number / 2)
    else:
        return (number * 3 + 1)

try:
    input = int(input("number: "))

    while(Collatz(input) != 1):
        input = Collatz(input)
        print(input)

except ValueError:
    print("Type integer value")
