# HW 8
def add_inventory(type_dictionary, widget_name, quantity):
    if widget_name not in type_dictionary:
        type_dictionary[widget_name] = quantity
        inventory_file = open('inventory.txt', 'w')
        inventory_file.write(str(type_dictionary) + '\n')
        inventory_file.close()
        print('\t*Data written to inventory.txt..')
    else:   # allows for value to be updated when using the same key.
        type_dictionary[widget_name] += quantity
        inventory_file = open('inventory.txt', 'w')
        inventory_file.write(str(type_dictionary) + '\n')
        inventory_file.close()
        print('\t*Quantity has been updated..')

def display_inventory():
    file_name = open('inventory.txt', 'r')
    file_contents = file_name.readline()
    file_name.close()
    print('File Contents')
    print(file_contents)