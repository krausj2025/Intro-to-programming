input_list = [1,2,3,4,5,6,7,8,9,10] 

def filter_list(input_list, threshold): 
    return [x for x in input_list if x <= threshold] 

print(filter_list(input_list, 6))
