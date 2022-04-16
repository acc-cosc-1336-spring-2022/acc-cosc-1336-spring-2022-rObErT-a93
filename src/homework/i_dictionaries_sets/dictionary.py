# Homework 7

def add_inventory(type_dictionary, widget_name, quantity):
    if widget_name not in type_dictionary:
        type_dictionary[widget_name] = quantity
    else:
        type_dictionary[widget_name] += quantity
    return type_dictionary

def remove_inventory_widget(type_dictionary, widget_name):
    if widget_name in type_dictionary:
        del type_dictionary[widget_name]
        print(widget_name,': Record DELETED')
    else:
        print('ITEM NOT FOUND')
    return type_dictionary

# Homework 6
def get_p_distance(list1, list2):
    index = 0
    diff = 0
    while index < len(list1):
        if list1[index] != list2[index]:
            diff += 1
        index += 1
    p_dist = diff / len(list1)
    return p_dist

def get_p_distance_matrix(list1):
    p_distance_matrix = []
    for r in list1:
        row = []
        for c in list1:
            row.append(get_p_distance(r,c))
        p_distance_matrix.append(row)
    return p_distance_matrix