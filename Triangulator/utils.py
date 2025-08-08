def lengthiest(list): 
    # Finds the element in a list with the largest length
    largest = len(str(list[0]))
    k = 0
    for i in range(len(list)):
        if len(str(list[i])) > largest:
            largest = len(str(list[i]))
            k = i
    return k, largest   # returns the index of the largest element and its length
    
def center_pad_list(list):

    center_padded_list = []
    l, largest = lengthiest(list)
    universal_space = len(str(list[l]))

    for i in range(len(list)):
        relative_length = universal_space - len(str(list[i]))

        if relative_length % 2 == 0:        
            # if even
            item = ' ' * (relative_length // 2) + str(list[i]) + ' ' * (relative_length // 2)

        else:
            # if odd
            item = ' ' * (relative_length // 2 + 1) + str(list[i]) + ' ' * (relative_length // 2)

        center_padded_list.append(item)
    return center_padded_list