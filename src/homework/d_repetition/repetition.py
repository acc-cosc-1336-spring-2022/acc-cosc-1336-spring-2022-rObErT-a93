def get_factorial(num):
    result = 1
    for i in range(1,num+1):
        result *= i
    return result

def sum_odd_numbers(num):
    counter = 0
    sum = 0
    while (counter < num):
        counter += 1
        if counter % 2 == 1:
            sum += counter
    return sum