import decisions

print()
num = int(input('Enter a number: '))
if(decisions.is_even(num)):
    print(num, 'is even!')
else:
    print(num, 'is odd!')
print('Numbers are FUN!')
print()

# Lecture 2.15.2022
num = int(input('Enter grade: '))
print(decisions.get_letter_grade(num))
print()

min = 1
max = 10
num = int(input('Enter a number: '))
result = decisions.number_is_in_range_and(min, max, num)
if(result):
    print(num, "is in range.")
else:
    print(num, "is not in range")