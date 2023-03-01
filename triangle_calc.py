from math import sin, asin, acos, radians, degrees, ceil


def law_of_cosines(side_1, side_2, side_3):

    # Law of Cosines: c^2 = a^2 + b^2 - 2ab * cos(theta)
    # Law of Cosines: side_1^2 = side_2^2 + side_3^2 - 2(side_2)(side_3) * cos(theta)

    side_1_squared = side_1**2
    side_2_squared = side_2**2
    side_3_squared = side_3**2

    side_2_side_3_by_2 = -2*side_2*side_3
    side_2_plus_side_3 = side_2_squared + side_3_squared
    side_1_minus_sides_2_3 = side_1_squared - side_2_plus_side_3
    divided_by = side_1_minus_sides_2_3 / side_2_side_3_by_2

    angle_1 = acos(divided_by)
    angle_1_radians = angle_1
    angle_1_degrees = degrees(angle_1)

    print(f"angle_1: {angle_1_radians} radians, {angle_1_degrees} degrees")

    return angle_1_radians


def law_of_sines_1_angle_3_sides(angle_1, side_1, side_2, side_3):

    # Law of Sines: sin a/A = sin b/B = sin c/C
    # Law of Sines: sin(angle_1)/side_1 = sin(angle_2)/side_2 = sin(angle_3)/side_3

    print(f"angle_1: {angle_1} radians")
    print(f"side_1: {side_1}")
    print(f"side_2: {side_2}")
    print(f"side_3: {side_3}")
    print("////////////////////////////////")

    angle_2 = asin(side_2/side_1 * sin(angle_1))
    angle_3 = radians(180) - (angle_1 + angle_2)

    angles_2_and_3 = [angle_2, angle_3]
    print(angles_2_and_3)

    return angles_2_and_3


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


def triangle_calc(num_angles, num_sides, angle_1, angle_2, angle_3, side_1, side_2, side_3):

    if num_angles == 0 and num_sides == 3:
        angle_1_radians = law_of_cosines(side_1, side_2, side_3)

        angles_2_and_3_radians = law_of_sines_1_angle_3_sides(angle_1_radians, side_1, side_2, side_3)

        all_angles = [round(angle_1_radians, 6),
                      round(angles_2_and_3_radians[0], 6),
                      round(angles_2_and_3_radians[1], 6)]

        all_angles_degrees = [round(degrees(angle_1_radians), 6),
                              round(degrees(angles_2_and_3_radians[0]), 6),
                              round(degrees(angles_2_and_3_radians[1]), 6)]
        print(all_angles)
        print(all_angles_degrees)

    elif num_angles == 1 and num_sides == 2:
        result = law_of_sines_1_angle_2_sides(angle_1, side_1, side_2)

        print(f"angle_2: {round(result[0], 6)} radians, {degrees(result[0])} degrees \n"
              f"angle_3: {round(result[1], 6)} radians, {degrees(result[1])} degrees \n"
              f"side_3: {round(result[2], 6)} units")




triangle_calc(num_angles=1, num_sides=2, angle_1=0.698132, angle_2=None, angle_3=None,
              side_1=30, side_2=40, side_3=None)
