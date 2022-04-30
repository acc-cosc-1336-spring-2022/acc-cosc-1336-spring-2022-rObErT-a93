#output comments variables input calculations output constants
def display_output(): #void function
    print('hello')

def test_config(): #value return function
    return True

def add_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

def integer_division(num1, num2):
    return num1 // num2   

def float_division(num1, num2):
    return num1 / num2

def operator_precedence_1(num1, num2, num3): # no paranthesis
    return num1 + num2 / num3

def operator_precedence_2(num1, num2, num3): # w/ paranthesis
    return (num1 + num2) / num3

def exponentiate_me(num1, num2):
    return num1 ** num2

def get_remainder(num1, num2):
    return num1 % num2