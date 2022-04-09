import dictionary

def main_menu():
    print('Main Menu')
    print('[1]: Get Distance Matrix')
    print('[2]: Exit')
    user_input = input('Select an option: ')
    if user_input == '1':
        option1()
    elif user_input == '2':
        option2()
    else:
        print('You have entered an invalid entry')
        print()
        main_menu()

def option1():
    print()
    print('Calculating Distance Matrix\n' 'Enter at least 2 sequences of DNA, maximum of 10 characters each.')
    dataset = []
    add_sequence = 'Y'
    while add_sequence == 'y' or add_sequence == 'Y':
        dna_sequence = input('Enter the sequence of DNA: ')
        dna_list = list(dna_sequence)
        dataset.append(dna_list)
        print('Continue adding data?\n' 'Only continue if at least 2 sequences have been added.')
        print()
        add_sequence = input('Enter y to continue or n to calculate: ')
    print()
    print('Here is the data entered.')
    for data in dataset:
        print('\t', data)
    print()
    print('The Distance Matrix of the data provided is: ')
    p_distance_matrix = dictionary.get_p_distance_matrix(dataset)
    for row in p_distance_matrix:
        for e in row:
            print(format(e, '12.1f'), end=' ')
        print('')
    print()
    user_input = input('Would you like to continue again? y/n: ')
    user_result = user_input
    if user_result == 'n' or user_result == 'N':
        main_menu()
    if user_result == 'y' or user_result == 'Y':
        option1()

def option2():
    print('Thank you....Goodbye')
    quit()

main_menu()