def second_largest_number(list_num):
    if len(list_num)<2:
        return None
    list_num.sort()
    return list_num[-2]
numlist=[3]
print (second_largest_number(numlist))
