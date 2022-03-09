#main program
from examples.h_strings.strings import string_sub_string
import strings

#strings.hello_world()
#strings.loop_string('hello')
#print()
#strings.loop_string_while('hello')

str = 'Four score and seven years ago'
sub_string = 'seven'

if string_sub_string(str, sub_string):
    print(sub_string + ' in ' + str)
else:
    print(sub_string + 'not in' + str)