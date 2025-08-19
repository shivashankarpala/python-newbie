list1 = 1
if type(list1) is list:
    print("list1 is a list")
else:
    print("list1 is not a list")

import pyperclip as pyclip

list = [1, 2, 30, 4, 5, 60, 7, 8, 900, 10]
universal_space = 3
n = 10
output_lines = []

for i in range(n):
    line = ' ' * (n - 1 - i) * universal_space  
    # Prints leading spaces for alignment

    for j in range(i + 1):
        # Print each element with a fixed width and separated with adequate spaces
        line += f'{str(list[j]):<{universal_space}}' + ' ' * (universal_space)

    output_lines.append(line)

print()

for line in output_lines:
    print(line) 

print()

#copy_prompt = input("Do you want to copy the output to clipboard? (y/n): ").strip().lower()
#if copy_prompt == 'y':
#    pyclip.copy(output)
#    print("Output copied to clipboard")


reverse_prompt = input("Do you want to reverse the output? (y/n): ").strip().lower()
if reverse_prompt == 'y':
    for line in output_lines[::-1]:
        print(line)
