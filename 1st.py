while True:
        try:
            num_1 = int(input("Please enter a number: "))
            break
        except:
            print("Error! Please put a valid number. ")

while True:
        try:
            num_2 = int(input("Please enter another number: "))
            break
        except:
            print("Error! Please put a valid number. ")

highest_num = num_1
if num_2 > highest_num:
    highest_num = num_2

print(highest_num)


    


