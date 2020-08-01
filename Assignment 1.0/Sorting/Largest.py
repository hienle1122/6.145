def largest_number(input_list):
    best_so_far = 0
    for i in range(len(input_list)):
        if input_list[i] > best_so_far:
            best_so_far = input_list[i]
    return (best_so_far)

