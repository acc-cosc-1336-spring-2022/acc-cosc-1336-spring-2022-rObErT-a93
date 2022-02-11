def test_config():
    return True

def is_even(num):
    return num % 2 == 0 # boolean expression; it returns True/False.

def get_letter_grade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'F'