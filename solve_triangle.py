from math import sin, cos, asin, acos, radians, degrees


def solve_triangle_1_side_2_angles(side_1, angle_1, angle_2):
    print("Hello, I have 1 side and 2 angles")


def solve_triangle_3_sides(side_1, side_2, side_3):
    print("Hello, I have three sides an no angles")


def triangle_calc():
    """Solves a triangle using the law of sines and law of cosines with user inputted side lengths
    and angles"""

    num_sides = 0
    num_angles = 0

    known_sides = int(input("How many sides are known? "))

    if known_sides > 3 or known_sides < 0:
        print("Please enter a value between 0 and 3.")

    elif known_sides == 1:
        num_sides += 1
        chosen_side = input("Please chose a side [a], [b], [c]: ")
        if chosen_side.lower() == "a":
            side_a = float(input("Please enter a value for side a: "))
        if chosen_side.lower() == "b":
            side_b = float(input("Please enter a value for side b: "))
        if chosen_side.lower() == "c":
            side_c = float(input("Please enter a value for side c: "))

    elif known_sides == 2:
        num_sides += 2
        chosen_side_1 = input("Please chose a side [a], [b], [c]: ")
        if chosen_side_1.lower() == "a":
            side_a = float(input("Please enter a value for side a: "))
        if chosen_side_1.lower() == "b":
            side_b = float(input("Please enter a value for side b: "))
        if chosen_side_1.lower() == "c":
            side_c = float(input("Please enter a value for side c: "))

        chosen_side_2 = input("Please chose a side [a], [b], [c]: ")
        if chosen_side_2.lower() == "a":
            side_a = float(input("Please enter a value for side a: "))
        if chosen_side_2.lower() == "b":
            side_b = float(input("Please enter a value for side b: "))
        if chosen_side_2.lower() == "c":
            side_c = float(input("Please enter a value for side c: "))

    elif known_sides == 3:
        num_sides += 3
        side_a = float(input("Please enter a value for side a: "))
        side_b = float(input("Please enter a value for side b: "))
        side_c = float(input("Please enter a value for side c: "))

    known_angles = int(input("How many angles are known? "))

    if known_angles > 3 or known_sides < 0:
        print("Please enter a value between 0 and 3.")

    elif known_angles == 1:
        num_angles += 1
        chosen_angle = input("Please chose an angle [A], [B], [C]: ")
        if chosen_angle.upper() == "A":
            angle_a = float(input("Please enter a value for angle a: "))
        if chosen_angle.upper() == "B":
            angle_b = float(input("Please enter a value for angle b: "))
        if chosen_angle.upper() == "C":
            angle_c = float(input("Please enter a value for angle c: "))

    elif known_angles == 2:
        num_angles += 2
        chosen_angle_1 = input("Please chose an angle [A], [B], [C]: ")
        if chosen_angle_1.upper() == "A":
            angle_a = float(input("Please enter a value for angle a: "))
        if chosen_angle_1.upper() == "B":
            angle_b = float(input("Please enter a value for angle b: "))
        if chosen_angle_1.upper() == "C":
            angle_c = float(input("Please enter a value for angle c: "))

        chosen_angle_2 = input("Please chose a side [A], [B], [C]: ")
        if chosen_angle_2.upper() == "A":
            angle_a = float(input("Please enter a value for angle A: "))
        if chosen_angle_2.upper() == "B":
            angle_b = float(input("Please enter a value for angle B: "))
        if chosen_angle_2.upper() == "C":
            angle_c = float(input("Please enter a value for angle C: "))

    else:
        num_angles += 3
        angle_a = float(input("Please enter a value for angle A: "))
        angle_b = float(input("Please enter a value for angle B: "))
        angle_c = float(input("Please enter a value for angle C: "))




triangle_calc()