print("Enter the first number and the symbol and the second number after that you will get your number will be executed")
number_One = int(input("enter the first number =  "))
symbol = input("enter the symbol = ")
number_Two = int(input("enter the second number = "))

while True:
    if symbol == '+':
        result = number_One + number_Two
        print(result)
    else:
        print("noh i can't ")
        result = '' 
    if result == '':
        print("noh try again")
        break
    else:
        print("yeh this is the calculation")
        break

for i in range(6):
    print(i * '*')