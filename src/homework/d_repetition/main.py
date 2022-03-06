import repetition

def menu():
    print('Homework 3 Menu')
    print('[1] Factorial')
    print('[2] Sum of Odd Numbers')
    print('[3] Exit')
    choice = int(input('Enter an option: '))
    while choice != 3:
        if choice == 1:
            print()
            print('[1]: Calculating Factorial')
            num = int(input('Enter a value to calculate factorial: '))
            result = repetition.get_factorial(num)
            if num < 0 or num > 10:
                print('Invalid entry {enter a value between 0 and 10}, Please try again!')
            elif(result):
                print('The Factorial = ', repetition.get_factorial(num))
            choice = int(input('Enter an option: '))

        elif choice == 2:
            print()
            print('[2]: Sum of Odd Numbers')
            num = int(input('Enter a value to calculate the sum of odd numbers: '))
            result = repetition.sum_odd_numbers(num)
            if num < 0 or num > 100:
                print('Invalid entry {enter a value between 0 and 100}, Please try again!')
            elif(result):  
                print('The Sum of Odd Numbers = ', repetition.sum_odd_numbers(num))
            choice = int(input('Enter an option: '))

        else:
            print('You have made in invalid selection.')
        choice = int(input('Enter an option: '))

def prompt_user():
    print('Would you like to calculate again? y or n: ')
    print('[1]: Calculate again')
    print('[2]: Main Menu')
    cont_again = int(input('Enter an option: '))
    while cont_again != 2:
        if cont_again == 1:
            print()
            print('[1]: Calculating')
            num = int(input('Enter a value to calculate factorial: '))
            result = repetition.get_factorial(num)
            if num < 0 or num > 10:
                print('Invalid entry {enter a value between 0 and 10}, Please try again!')
            elif(result):
                print('The Factorial = ', repetition.get_factorial(num))

menu()
