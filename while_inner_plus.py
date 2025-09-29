input_list = [1,2,3,4,5,6,7,8,9,10,[11,12,13,14,15,[16,17,18,19,20]]]
def inner_plus_one(input_list):
    current = input_list    #this will narrow down until the innermost list is found
    while any(isinstance(x, list) for x in current): 
        for x in current:
            if isinstance(x, list):
                current = x
                break  # Now current represents the inner most list now add one to each element
    return [ x + 1 for x in current]

print(inner_plus_one(input_list))