import math     # python built in library
import random   # python built in library

def test_config():
    return True

def local_variable(val0):
    val = val0
    val0 = 100
    return val    

def main():
    val = 0 # example
    local_variable()

val3 = 10
def use_global():       # Global Variable
    val3 = 5
    print(val3)

def get_random_number(min, max):
    return random.randint(min, max) # python buil in library function

#random.seed(10)
def display_random_numbers(min, max, cnt):  # void function
    for i in range(cnt):
        print(random.randint(min, max))

def return_first_and_last_name():
    return 'john', 'doe'