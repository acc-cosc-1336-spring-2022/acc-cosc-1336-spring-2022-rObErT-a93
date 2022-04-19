# Lecture 4/12
def open_file(file_name):
    try:
        # Work with the file.
        file_handle = open(file_name, 'r')
        print('File opened.')
        total = 0

        for line in file_handle:
            amount = float(line)
            total += amount
        
        print('Total: ', total)
        # Close the file.
    except FileNotFoundError:
        print('File:', file_name ,'does not exist.')

    except ValueError as err:
        print(err)
        #print('File contains invalid data.')

    else:
        print('No errors occurred.')