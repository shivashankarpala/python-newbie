import utils

def print_equilateral_triangle(n, list, style, row_reversed = False, column_reversed = False):

    # Limit the n to the length of the list
    if n > len(list):
        n = len(list)

    if column_reversed:
        list.reverse()

    output_lines = []
    l, largest = utils.lengthiest(list)
    universal_space = len(str(list[l]))     # Universal space is the length of the longest element in the list
    centered_list = utils.center_pad_list(list)

    if style == 1:
        for i in range(n):
            item = ' ' * (n - 1 - i) * universal_space
            # Prints leading spaces for alignment

            for j in range(i + 1):
                # Print each element with a fixed width and separated with adequate spaces
                item += centered_list[i] + ' ' * universal_space

            output_lines.append(item)

    elif style == 2:
        for i in range(n):
            item = ' ' * (n - 1 - i) * universal_space
            # Prints leading spaces for alignment

            for j in range(i + 1):
                # Print each element with a fixed width and separated with adequate spaces
                item += centered_list[j] + ' ' * universal_space
            
            output_lines.append(item)
    
    if row_reversed:
        utils.print_triangle(output_lines, row_reversed=True)
    else:
        utils.print_triangle(output_lines)


#    elif style == 2:
#        for i in range(n):
#            for j in range(n - i - 1):
#                print(' ', end=' ')
#            for j in range(i + 1):
#                print(f'{str(list[i]):^{universal_space}}', end=' ')
#           print()
# This style is not implemented in the original code, but can be added if needed

def print_right_triangle(n, list, side, row_reversed = False, column_reversed = False):

    # Limit the n to the length of the list
    if n > len(list):
        n = len(list)

    if column_reversed:
        list.reverse()

    output_lines = []
    l, largest = utils.lengthiest(list)
    universal_space = len(str(list[l]))
    centered_list = utils.center_pad_list(list)

    if side == 1:
        
        # Right-angled triangle with the right angle at the top left
        for i in range(n):
            item = ''
            for j in range(n - i):
                item += centered_list[j] + ' '
            output_lines.append(item)

    elif side == 2:

        # Right-angled triangle with the right angle at the bottom left
        for i in range(n):
            item = ''
            for j in range(i + 1):
                item += centered_list[j] + ' '
            output_lines.append(item)

    elif side == 3:

        # Right-angled triangle with the right angle at the top right
        for i in range(n):
            item = ' ' * i * (universal_space + 1)
            for j in range(n-i):
                item += centered_list[i+j] + ' '
            output_lines.append(item)

    elif side == 4:

        # Right-angled triangle with the right angle at the bottom right
        for i in range(n):
            item = ' ' * (n - 1 - i) * (universal_space + 1)
            for j in range(n-i-1, n):
                item += centered_list[j] + ' '
            output_lines.append(item)
    
    if row_reversed:
        utils.print_triangle(output_lines, row_reversed=True)
    else:
        utils.print_triangle(output_lines)