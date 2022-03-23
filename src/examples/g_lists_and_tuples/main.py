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