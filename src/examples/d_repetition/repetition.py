from tkinter.tix import MAX


def test_config():
    return True

def display_numbers(num):
    cnt = 0
    while cnt < num:
        print(cnt + 1)
        cnt = cnt + 1 # statement that makes the boolean expression cnt < num false

def sum_of_squares(num):
    cnt = 0
    sum = 0
    while cnt <= num:
        sum = sum + cnt**2
        cnt += 1 # statment to make boolean expression false
    return sum 

def prompt_user():
    keep_going = 'y'
    while keep_going == 'y':
        keep_going = input("Loop again, type y? ") # statement to make boolean expression false

def for_intro_loop():
    for num in [1,2,3,4,5]:
        print(num)

def for_intro_loop_strings():
    for name in ['Winken', 'Blinken', 'Nod']:
        print(name)

def for_num_range(val):
    for num in range(val):
        print(num)

def for_num_range_w_start_value(num, num1):
    for val in range(num, num1):
        print(val)

def for_display_sum_of_squares(num, num1):
    for val in range(num, num1):
        square = val ** 2
        print(val, '\t', square)

def get_sum(num): # Running Total
    sum = 0
    count = 0
    while(count <= num):
        sum += count
        count += 1
    return sum

def get_sum_for(num):
    sum = 0
    for n in range(num):
        sum += n + 1
    return sum

def demo_sentinel():
    lot_number = 10
    while lot_number != 0:
        lot_number = int(input('Enter lot number or zero to exit: '))
        print(lot_number)

