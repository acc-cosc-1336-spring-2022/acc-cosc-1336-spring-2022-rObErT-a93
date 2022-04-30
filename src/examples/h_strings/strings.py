def test_config():
    return True

def hello_world():
    hello = 'Hello World!'  # string = sequence of characters or symboles
    print(hello[0])     # 0 = index
    print(hello)

def loop_string(str):
    for c in str:   # hello
        print(c)

def loop_string_while(str):
    index = 0
    while index < len(str):
        print(str[index])
        index = index + 1

def concat_strings(str1, str2):
    return str1 + str2

def slice_str(str):
    return str[6:10]

def string_sub_string(str, sub_string):
    return sub_string in str