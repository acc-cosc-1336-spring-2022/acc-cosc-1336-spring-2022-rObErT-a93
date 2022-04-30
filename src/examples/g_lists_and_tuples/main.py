import lists

nums = [99,100,101,102]

lists.loop_list_w_for(nums)
print('----------')
for n in nums:
    print(n)

print('*************')

num = [99,100,101,102]
lists.loop_list_w_while(num)
print('----------')
for n in num:
    print(n)

print('**************')

lists.collect_home_values()

print('-----------------3/24 Lecture------------------------')
print()
list1 = ["C++", "C#", "Python", "Java"]
item1 = input('Enter item to find: ')

result = lists.find_items_in_lists(item1, list1)

if(result):
    print(item1, 'in the list')

else:
    print(item1, 'not in the list')

