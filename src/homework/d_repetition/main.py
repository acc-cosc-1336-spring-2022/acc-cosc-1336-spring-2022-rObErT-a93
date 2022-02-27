import repetition

print('Homework 3 Menu')
def menu():
    print('[1] Factorial')
    print('[2] Sum of Odd Numbers')
    print('[3] Exit')

def prompt_user():
    try_again = 'y'
    while try_again != 'n':
        try_again = input('Would you like to run program again?, y or n: ')

menu()
option = int(input('Enter an option: '))
print()
while option != 3:
    if option == 1:
        print()
        print('[1]: Calculating Factorial')
        num = int(input('Enter a value to calculate factorial: '))
        result = repetition.get_factorial(num)
        if num < 0 or num > 10:
            print('Invalid entry {enter a value between 0 and 10}, Please try again!')
        elif(result):
            print('The Factorial = ', repetition.get_factorial(num))
    elif option == 2:
        print()
        print('[2]: Sum of Odd Numbers')
        num = int(input('Enter a value to calculate the sum of odd numbers: '))
        result = repetition.sum_odd_numbers(num)
        if num < 0 or num > 100:
            print('Invalid entry {enter a value between 0 and 100}, Please try again!')
        elif(result):  
            print('The Sum of Odd Numbers = ', repetition.sum_odd_numbers(num))
    else:
        print('You have made in invalid selection.')
    print()
    print('Homework 3 Menu')
    menu()
    option = int(input('Enter an option: '))