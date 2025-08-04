import triangle

print("------------------------------Triangulator------------------------------")

n = int(input("Number of Rows: "))
list = [1, 20, 3, 40, 5, 60, 7, 8, 9, 100]

print()
print("Select Triangle: ")
print("1. Equilateral Triangle")
print("2. Right-Angled Triangle")

choice = int(input("Enter your choice (1 or 2): "))
print()


if choice == 1:

    print("Select Style of Equilateral Triangle: ")
    print("1. Each row each element")
    print("2. Each row with all elements")

    type = int(input("Enter your choice (1 or 2): "))
    print()

    triangle.print_equilateral_triangle(n, list, type)

elif choice == 2:

    print("Select Right-Angled Triangle Orientation: ")
    print("Right Angle at: ")
    print("1. Top Left")
    print("2. Bottom Left")
    print("3. Top Right")
    print("4. Bottom Right")
    side = int(input("Enter your choice (1-4): "))
    print()

    triangle.print_right_triangle(n, list, side)

print("------------------------------------------------------------------------")
