# i have to do the projects with the loops and the conditions and the functions for right now 
# question = how does the conversion works in the python why does the string math sign is not equal to the string like the js 

print("Enter the first number and the symbol and the second number after that you will get your number will be executed")
number_One = int(input("enter the first number =  "))
symbol = input("enter the symbol = ")
number_Two = int(input("enter the second number = "))

#Execution process: 
if symbol == '+':
    sum = number_One + number_Two
    print(sum)
elif symbol == '-':
    less = number_One - number_Two
    print(less)
elif symbol == '*':
    times = number_One * number_Two
    print(times)
elif symbol == '/':
    divison = number_One / number_Two
    print(divison)
elif symbol == '%':
    modulas = number % number_Two
    print(modulas)
else:
    print("Enter the integer value only😭")
