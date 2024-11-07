while True:
    try:
        num_1 = int(input("Please input a number: "))
        break
    except:
        print("Error! Please input a valid number")

while True:
    try:
        num_2 = int(input("Please input a number: "))
        break
    except:
        print("Error! Please input a valid number")

lowest_num = num_1
if num_2 < num_1:
    lowest_num = num_2

print("The lowest number is", lowest_num)