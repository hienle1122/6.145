def flatten(array):
    flat_list = []
    for i in array:
        if type(i) != list:
            flat_list.append(i)
        else:
            f = flatten(i)
            for e2 in f:
                flat_list.append(e2)
    return flat_list
 
 
def run_length_encode_2d(array):
    x = flatten(array)
    count = 1
    out = []
 
    if len(x) == 1:
        out.append((count, x[0]))
 
    for i in range(1, len(x)):
 
        if x[i] == x[i - 1]:
            count = count + 1
 
        else:
            out.append((count, x[i - 1]))
            count = 1
 
        # prints last digit
        if i == len(x) - 1:
            out.append((count, x[i]))
 
    return out
    
    
