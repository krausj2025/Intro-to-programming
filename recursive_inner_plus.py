input_list = [1,2,3,4,5,6,7,8,9,10,[11,12,13,14,15,16,[17,18,19,20]]]

def inner_recursive(input_list):
    for x in input_list:
        if isinstance(x, list):
            return inner_recursive(x) #just in case the input list has no nested list inside
    return [x + 1 for x in input_list]
print(inner_recursive(input_list))