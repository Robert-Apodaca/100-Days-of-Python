number = input("Enter a positive integer:")
number = int(number)
for i in range(1,number + 1):
    if number % i == 0:
        print(f"{i} is a factor of number")


