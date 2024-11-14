even_count = 0

for i in range(10):
    while True:
        try:
            number = int(input("Pls input a number: "))
            break
        except ValueError:
            print("Error! Pls input a valid number")

    if number % 2 == 0:
        even_count += 1

print("The even numbers count is", even_count)
