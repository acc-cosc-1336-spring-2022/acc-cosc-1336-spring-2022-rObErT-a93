import files
# HW 8
def main_menu():
    print('Inventory Menu\n\t[1]: Add/Update Inventory\n\t[2]: Display Inventory\n\t[3]: Exit')
    user_input = input('Select an option: ')
    if user_input == '1':
        option1()
    elif user_input == '2':
        option2()
    elif user_input == '3':
        print('Thank you...Goodbye!.')

def option1():
    type_dictionary = {}
    print('\tAdd / Update Widget Inventory')
    try:
        widget_name = input('Enter Widget Name: ')
        quantity = int(input('Enter the quantity of Widget: '))
        widgets_dictionary = files.add_inventory(type_dictionary, widget_name, quantity)
        print('\tNOTE* To update Widget Quantity, CONTINUE & use the same Widget Name.')
    except ValueError:
        print('\tValueError: invalid literal for int() with base 10:\n','\t*Quantity must be a number.')
    user_choice = input('Would you like to continue?: ')
    while user_choice.lower() == 'y':
        try:
            widget_name = input('Enter Widget Name: ')
            quantity = int(input('Enter the quantity of Widget: '))
            widgets_dictionary = files.add_inventory(type_dictionary, widget_name, quantity)
            user_choice = input('\tWould you like to continue?: ')
        except ValueError:
            print('\tValueError: invalid literal for int() with base 10:\n','\t*Quantity must be a number.')
    if user_choice.lower() == 'n':
        main_menu()

def option2():
    print('Display File Data.')
    found = False
    print('\tFile Directory:\n'  + 
            '\t\t1 of 1: inventory.txt')
    search = input('Enter a file name to view: ')
    file_name = ('inventory.txt')
    if file_name == search:
        files.display_inventory()
        found = True
    if file_name != search:
        print('Could not find file name', search)
    user_choice = input('Would you like to search another file? ')
    while user_choice.lower() == 'y':
        found = False
        print('\tFile Directory:\n' + 
                '\t\t1 of 1: inventory.txt')
        search = input('Enter a file name to search for: ')
        file_name = ('inventory.txt')
        if file_name == search:
            files.display_inventory()
            found = True
        if file_name != search:
            print('Could not find file name', search)
        user_choice = input('Would you like to search another file? ')
    if user_choice.lower() == 'n':
        main_menu()

def option3():
    print('Thank you.....Goodbye!')
    quit()

main_menu()