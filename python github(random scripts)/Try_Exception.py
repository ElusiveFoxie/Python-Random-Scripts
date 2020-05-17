def devide(DevideBy):
    try:
        result = 50 / DevideBy
        print (result)
    except ZeroDivisionError:
        print("Can't devide by 0")

devide(30)
devide(0)
devide(10)
devide(20)
devide(5)
