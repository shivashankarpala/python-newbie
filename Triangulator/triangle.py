# Finds the element in a list with the largest length
def lengthiest(list): 

    largest = len(str(list[0]))
    k = 0
    for i in range(len(list)):
        if len(str(list[i])) > largest:
            largest = len(str(list[i]))
            k = i
    return k, largest
    # returns the index of the largest element and its length

def print_equilateral_triangle(n, list, style):

    # Limit the n to the length of the list
    if n > len(list):
        n = len(list)


    l, largest = lengthiest(list)
    universal_space = len(str(list[l])) 
    # Universal space is the length of the longest element in the list

    if style == 1:
        for i in range(n):
            print(' ' * (n - 1 - i) * universal_space, end='')
            # Prints leading spaces for alignment

            for j in range(i + 1):

                # If the element is less than the universal space, it will be padded with spaces
                # All elements will have the same length when printed
                if (len(str(list[i])) < universal_space):
                    print(str(list[i]) + ' ' * (universal_space - 1), end=' ' * universal_space)
                else:
                    print(list[i], end=' ' * universal_space)
                    
            print() # New line after each row of the triangle

    elif style == 2:
        for i in range(n):
            for j in range(n - i - 1):
                print(' ', end=' ')
            for j in range(i + 1):
                print(str(list[j])  + ' ' * (universal_space - len(str(list[j]))), end=' ')
            print()

def print_right_triangle(n, list, side):

    # Limit the n to the length of the list
    if n > len(list):
        n = len(list)

    l, largest = lengthiest(list)
    universal_space = len(str(list[l]))

    if side == 1:
        
        # Right-angled triangle with the right angle at the top left
        for i in range(n):
            for j in range(n - i):
                print(list[j], end=' ' * universal_space)
            print()
        

    elif side == 2:

        # Right-angled triangle with the right angle at the bottom left
        for i in range(n):
            for j in range(i + 1):
                print(list[j], end=' ' * universal_space) 
            print()
    
    elif side == 3:

        # Right-angled triangle with the right angle at the top right
        for i in range(n):
            print(' ' * (n - 1 - i) * (universal_space + 1), end='')
            for j in range(i + 1):
                print(str(list[j]) + ' ' * (universal_space + 1 - len(str(list[j]))), end='')
            print()

    elif side == 4:

        # Right-angled triangle with the right angle at the bottom right
        for i in range(n):
            print(' ' * i * (universal_space + 1), end='')
            for j in range(n - i):
                print(str(list[j]) + ' ' * (universal_space + 1 - len(str(list[j]))), end='')
            print()