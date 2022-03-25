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

def find_items_in_lists(item1, list1):      # 3/24 Lecture
    if item1 in list1:
        return True     # allows for function to be testable
    else:
        return False

def append_item_to_list(item1, list1):
    list1.append(item1)