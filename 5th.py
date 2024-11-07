def get_10_numbers(number_input):
    while True:
        try:
            return int(input(number_input))
        except:
            print("Error! Please input a valid number.")

num_1 = get_10_numbers("Please input a number: ")
num_2 = get_10_numbers("Please input a number: ")
num_3 = get_10_numbers("Please input a number: ")
num_4 = get_10_numbers("Please input a number: ")
num_5 = get_10_numbers("Please input a number: ")
num_6 = get_10_numbers("Please input a number: ")
num_7 = get_10_numbers("Please input a number: ")
num_8 = get_10_numbers("Please input a number: ")
num_9 = get_10_numbers("Please input a number: ")
num_10 = get_10_numbers("Please input a number: ")


total_difference = (num_1 - num_2 - num_3 - num_4 - num_5 - num_6 - num_7 - num_8 - num_9 - num_10)
print("The difference is:", total_difference)




