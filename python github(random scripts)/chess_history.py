turn = ["White: ", "Black: "]
x = input(turn[0])
chess = {}
i = 1
while (x != ""):
    if (i%2==0):
        chess[str(i)+":"] = str(x)
        i+=1
        x = input(turn[0])
    else:
        chess[str(i) + ":"] = str(x)
        i += 1
        x = input(turn[1])
print (chess)