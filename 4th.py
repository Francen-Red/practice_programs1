while True:
    try:
        num_1 = int(input("Please input a number: "))
        break
    except:
        print("Error! Please input a valid number")

while True:
    try:
        num_2 = int(input("Please input a number for exponent: "))
        break
    except:
        print("Error! Please input a valid number")

print("The result is:", num_1 ** num_2)
