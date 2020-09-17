operation = input(''' please type in the math operation you would liketo complete:
+ for addition
- for subtraction
* for multiplication
/ for divison
''')

number_1 = int(input('enter your first number: '))
number_2 = int(input('enter your second number: '))

if operation == '+':+=
    print('{} + {} ='.format(number_1, number_2))
    print(number_1 + number_2)

elif operation == '-':
    print('{} + {} ='.format(number_1, number_2))
    print(number_1 - number_2)

elif operation == '*':
    print('{} + {} ='.format(number_1, number_2))
    print(number_1 * number_2)

elif operation == '/':
    print('{} + {} ='.format(number_1, number_2))
    print(number_1 / number_2)

else:
    print('you have not typed a valid operator, please run the program again.')
