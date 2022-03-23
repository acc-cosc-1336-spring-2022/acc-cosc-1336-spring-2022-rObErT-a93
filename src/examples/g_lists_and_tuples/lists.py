def test_config():
    return True

def loop_list_w_for(nums):
    for n in nums:
        print(n)

    nums[0] = 10

def loop_list_w_while(num):
    indx = 0

    while indx < len(num):
        print(num[indx])
        indx += 1

def collect_home_values():
    home_values = [0] * 5
    indx = 0
    while indx < len(home_values):      # while loops will change the original value in lists []
        home_values[indx] = int(input('Enter Home Value: '))
        indx += 1

    for v in home_values:   # for loop does not change original value in lists []
        print(v)