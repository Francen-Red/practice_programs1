while True:
    try:
        num_1 = int(input("Please input a number: "))
        break
    except:
        print("Error! Please input a valid number")

while True:
    try:
        num_2 = int(input("Please input another number: "))
        break
    except:
        print("Error! Please input a valid number")

print("The product is:", num_1 // num_2)
