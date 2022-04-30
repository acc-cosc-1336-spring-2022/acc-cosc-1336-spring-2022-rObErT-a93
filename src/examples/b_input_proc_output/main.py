import input_process_output

#input_process_output.display_output()
#input_process_output.test_config()
#input_process_output.add_number()

val0 = 'joe'
char1 = 'j'

print(val0)

num1 = int(input('enter num1: '))
num2 = int(input('enter num2: '))
num3 = int(input('enter num3: '))

print(input_process_output.add_numbers(num1,num2)) #parameters give us flexibility/reuse
print(input_process_output.multiply_numbers(num1, num2))
print(input_process_output.integer_division(num1, num2))
print(input_process_output.float_division(num1, num2))
print(input_process_output.operator_precedence_2(num1, num2, num3))
print(input_process_output.get_remainder(num1, num2))
