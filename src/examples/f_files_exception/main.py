#main program
file_name = 'Programming.txt'

# creates the file
# programming_file = open(file_name, 'w') # writes to file
programming_file = open(file_name, 'a') # appends to file

# uses the file
# programming_file.write('\tProgramming Languages\n')
# programming_file.write('C#\n')
# programming_file.write('Python\n')
# programming_file.write('Java\n')
    # appending to file with line 6
programming_file.write('C\n')
programming_file.write('Lisp\n')
programming_file.write('Ada\n')

# close the file
programming_file.close()

# open file for reading
programming_file = open(file_name, 'r')

# uses the file
for line in programming_file:
    print(line.rstrip('\n'))
#programming_file_contents = programming_file.read() 
# programming_file_contents = programming_file.readline() # returns individual line from file
# programming_file_contents += programming_file.readline() # += returns another line from file
# programming_file_contents += programming_file.readline()
# programming_file_contents += programming_file.readline()
# programming_file_contents += programming_file.readline()
# programming_file_contents += programming_file.readline()
# programming_file_contents += programming_file.readline()

programming_file.close()    # closes the file

# prints the content
#print(programming_file_contents)