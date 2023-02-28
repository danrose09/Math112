from math import sin, asin, radians, degrees


def law_of_sines_all_angles_one_side_degrees(angle_a, angle_b, angle_c, side_1):

    print(f"angle_a: {angle_a} degrees, {round(radians(angle_a), 6)} radians")
    print(f"angle_b: {angle_b} degrees, {round(radians(angle_b), 6)} radians")
    print(f"angle_c: {angle_c} degrees, {round(radians(angle_c), 6)} radians")
    print(f"side_1: {side_1} units")
    print("////////////////////////////////")
    side_2 = round(sin(radians(angle_b))/(sin(radians(angle_a))/side_1), 6)
    print(f"side_2: {side_2} units")

    side_3 = round(sin(radians(angle_c))/(sin(radians(angle_b))/side_2), 6)
    print(f"side_3: {side_3} units")
    return


def law_of_sines_one_angle_two_sides_degrees(angle_a, side_a, side_b):

    print(f"angle_a: {angle_a} degrees, {round(radians(angle_a), 6)} radians")
    print(f"side_a: {side_a} units")
    print(f"side_b: {side_b} units")
    print("////////////////////////////////")
    angle_b = asin((side_a/side_b)*sin(radians(angle_a)))
    angle_b = round(degrees(angle_b), 6)
    print(f"angle_b: {angle_b} degrees")
    return


# law_of_sines_all_angles_one_side_degrees(30, 105, 45, 2)
law_of_sines_one_angle_two_sides_degrees(angle_a=40, side_a=40, side_b=30)
