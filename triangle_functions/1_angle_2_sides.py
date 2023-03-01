from math import sin, asin, radians


def law_of_sines_1_angle_2_sides(angle_1, side_1, side_2):

    # Law of Sines: sin a/A = sin b/B = sin c/C
    # Law of Sines: sin(angle_1)/side_1 = sin(angle_2)/side_2 = sin(angle_3)/side_3

    print(f"angle_1: {angle_1} radians")
    print(f"side_1: {side_1}")
    print(f"side_2: {side_2}")

    print("////////////////////////////////")

    angle_2 = asin(side_2 / side_1 * sin(angle_1))
    angle_3 = radians(180) - (angle_1 + angle_2)

    side_3 = sin(angle_3) / (sin(angle_2) / side_2)

    result = [angle_2, angle_3, side_3]

    return result
