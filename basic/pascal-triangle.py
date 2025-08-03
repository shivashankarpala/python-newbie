import copy

def pascal_triangle(n):
    list = [[1]]
    line_list = [[1]]

    while len(list) <= n:
        temp_list = []

        for i in range(len(line_list)+1):
            if i == 0 or i == (len(line_list)):
                elem = 1
                temp_list.append(elem)
                    
            else:
                elem = line_list[i-1] + line_list[i]
                temp_list.append(elem)

        list.append(temp_list)
        line_list = copy.copy(temp_list)
    
    return list

def lengthiest(lst):

    largest = len(str(lst[0]))
    k = 0
    for i in range(len(lst)):
        if len(str(lst[i])) > largest:
            largest = len(str(lst[i]))
            k = i
    return k, largest

pascal_list = (pascal_triangle(12))

n = len(pascal_list) 
list = copy.deepcopy(pascal_list)
list_tail = list[-1]

l, largest = lengthiest(list_tail)
universal_space = len(str(list_tail[l])) 

for i in range(n):
    print(' ' * (n - 1 - i) * universal_space, end='')

    for j in range(i + 1):
        if (len(str(list[i][j])) < universal_space):
            print(str(list[i][j]) + ' ' * (universal_space - 1), end=' ' * universal_space)
        else:
            print(list[i][j], end=' ' * universal_space)
    print()