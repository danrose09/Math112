from math import sin, asin, degrees


def law_of_sines_all_angles_one_side(angle_a, angle_b, angle_c, side_1):

    print(f"angle_a: {angle_a}")
    print(f"angle_b: {angle_b}")
    print(f"angle_c: {angle_c}")
    print(f"side_1: {side_1}")
    print("////////////////////////////////")
    side_2 = round(sin(angle_b)/(sin(angle_a)/side_1), 6)
    print(f"side_2: {side_2}")

    side_3 = round(sin(angle_c)/(sin(angle_b)/side_2), 6)
    print(f"side_3: {side_3}")
    return


def law_of_sines_one_angle_two_sides(angle_a, side_a, side_b):

    print(f"angle_a: {angle_a} radians")
    print(f"side_a: {side_a}")
    print(f"side_b: {side_b}")
    print("////////////////////////////////")
    angle_b = asin((side_a/side_b)*sin(angle_a))
    angle_b = round(angle_b, 6)
    print(f"angle_b: {angle_b} radians")
    return


# law_of_sines_all_angles_one_side(0.523599, 1.8326, 0.785398, 2)
law_of_sines_one_angle_two_sides(0.698132, 40, 30)

