import utils

def print_equilateral_triangle(n, list, style):

    # Limit the n to the length of the list
    if n > len(list):
        n = len(list)


    l, largest = utils.lengthiest(list)
    universal_space = len(str(list[l])) 
    # Universal space is the length of the longest element in the list

    if style == 1:
        for i in range(n):
            print(' ' * (n - 1 - i) * universal_space, end='')
            # Prints leading spaces for alignment

            for j in range(i + 1):
                # Print each element with a fixed width and separated with adequate spaces
                print(f'{str(list[i]):^{universal_space}}', end=' ' * (universal_space))

            print() # New line after each row of the triangle

    elif style == 2:
        for i in range(n):
            print(' ' * (n - 1 - i) * universal_space, end='')
            # Prints leading spaces for alignment

            for j in range(i + 1):
                # Print each element with a fixed width and separated with adequate spaces
                print(f'{str(list[j]):^{universal_space}}', end=' ' * (universal_space))

            print() # New line after each row of the triangle     


#    elif style == 2:
#        for i in range(n):
#            for j in range(n - i - 1):
#                print(' ', end=' ')
#            for j in range(i + 1):
#                print(f'{str(list[i]):^{universal_space}}', end=' ')
#           print()
# This style is not implemented in the original code, but can be added if needed

def print_right_triangle(n, list, side):

    # Limit the n to the length of the list
    if n > len(list):
        n = len(list)

    l, largest = utils.lengthiest(list)
    universal_space = len(str(list[l]))

    if side == 1:
        
        # Right-angled triangle with the right angle at the top left
        for i in range(n):
            for j in range(n - i):
                print(f'{str(list[j]):^{universal_space}}', end=' ')
            print()
        

    elif side == 2:

        # Right-angled triangle with the right angle at the bottom left
        for i in range(n):
            for j in range(i + 1):
                print(f'{str(list[j]):^{universal_space}}', end=' ')
            print()
    
    elif side == 3:

        # Right-angled triangle with the right angle at the top right
        for i in range(n):
            print(' ' * i * (universal_space + 1), end='')
            for j in range(n-i):
                print(f'{str(list[i+j]):^{universal_space}}', end=' ')
            print()

    elif side == 4:

        # Right-angled triangle with the right angle at the bottom right
         for i in range(n):
            print(' ' * (n - 1 - i) * (universal_space + 1), end='')
            for j in range(n-i-1, n):
                print(f'{str(list[j]):^{universal_space}}', end=' ')
            print()