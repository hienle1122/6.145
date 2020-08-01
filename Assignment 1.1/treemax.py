list = []
def tree_max(tree):
    if len(tree['children']) == 0:
        list.append(tree['value'])
    else:
        for element in tree['children']:
            tree_max(element)
            list.append(tree['value'])
 
    return max(list)
