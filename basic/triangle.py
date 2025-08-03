# Finds the element in a list with the largest length
def lengthiest(lst): 

    largest = len(str(lst[0]))
    k = 0
    for i in range(len(lst)):
        if len(str(lst[i])) > largest:
            largest = len(str(lst[i]))
            k = i
    return k, largest
    # returns the index of the largest element and its length

n = 20
list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# Limit the n to the length of the list
if n > len(list1):
    n = len(list1)


l, largest = lengthiest(list1)
universal_space = len(str(list1[l])) 
# Universal space is the length of the longest element in the list

for i in range(n):
    print(' ' * (n - 1 - i) * universal_space, end='')
    # Prints leading spaces for alignment

    for j in range(i + 1):

        # If the element is less than the universal space, it will be padded with spaces
        # All elements will have the same length when printed
        if (len(str(list1[i])) < universal_space):
            print(str(list1[i]) + ' ' * (universal_space - 1), end=' ' * universal_space)
        else:
            print(list1[i], end=' ' * universal_space)
            
    print() # New line after each row of the triangle