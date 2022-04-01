#
import strings

def menu():
    print('Main Menu')
    print('[1] Hamming Distance')
    print('[2] DNA Complement')
    print('[3] Exit')
    user_input = input('Choose an option: ')
    if user_input == '1':
        option_1()
    elif user_input == '2':
        option_2()
    elif user_input == '3':
        option_3()

def option_1():
    print('Enter a 16 character sequence of DNA,')
    input_1 = input('Enter 1st DNA Sequence: ')
    input_2 = input('Enter 2nd DNA Sequence: ')
    result = strings.get_hamming_distance(input_1, input_2)
    print('The Hamming Distance = ', result)
    user_input = input('Would you like to continue again? y/n: ')
    user_result = user_input
    if user_result == 'n' or user_result == 'N':
        menu()
    if user_result == 'y' or user_result == 'Y':
        option_1()

def option_2():
    print('Enter a 10 character sequence of DNA')
    dna = input('Enter DNA sequence: ')
    result = strings.get_dna_complement(dna)
    print('DNA Complement = ', result)
    user_input = input('Would you like to continue again? y/n: ')
    user_result = user_input
    if user_result == 'n' or user_result == 'N':
        menu()
    if user_result == 'y' or user_result == 'Y':
        option_2()

def option_3():
    print('Thank you...Goodbye')
    quit()

menu()