from math import sin, asin, radians, degrees


def law_of_sines_all_angles_one_side_degrees(angle_1, angle_2, angle_3, side_1):

    print(f"angle_a: {angle_1} degrees, {round(radians(angle_1), 6)} radians")
    print(f"angle_b: {angle_2} degrees, {round(radians(angle_2), 6)} radians")
    print(f"angle_c: {angle_3} degrees, {round(radians(angle_3), 6)} radians")
    print(f"side_1: {side_1} units")
    print("////////////////////////////////")
    side_2 = round(sin(radians(angle_2))/(sin(radians(angle_1))/side_1), 6)
    print(f"side_2: {side_2} units")

    side_3 = round(sin(radians(angle_3))/(sin(radians(angle_2))/side_2), 6)
    print(f"side_3: {side_3} units")
    return


def law_of_sines_one_angle_two_sides_degrees(angle_1, side_1, side_2):

    print(f"angle_1: {angle_1} degrees, {round(radians(angle_1), 6)} radians")
    print(f"side_1: {side_1} units")
    print(f"side_b: {side_2} units")
    print("////////////////////////////////")
    angle_b = asin((side_1/side_2)*sin(radians(angle_1)))
    angle_b = round(degrees(angle_b), 6)
    print(f"angle_b: {angle_b} degrees")
    return


# law_of_sines_all_angles_one_side_degrees(angle_1=97, angle_2=31, angle_3=52, side_1=21.7)
law_of_sines_one_angle_two_sides_degrees(angle_1=85, side_1=4.2, side_2=6.41)
