def mirrored_right_angle_triangle(rows):
    for i in range(1, rows + 1):
        print(" " * (rows - i), end="")
        print("*" * i)
rows = int(input("Enter the number of rows for the mirrored triangle: "))
mirrored_right_angle_triangle(rows)