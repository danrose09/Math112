from math import sin, asin, acos, radians, degrees


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
    angle_1_radians = round(angle_1, 6)
    angle_1_degrees = round(degrees(angle_1), 6)

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

    angle_2 = round(angle_2, 6)

    angle_3 = radians(180) - (angle_1 + angle_2)
    angle_3 = round(angle_3, 6)

    angles_2_and_3 = [angle_2, angle_3]
    print(angles_2_and_3)
    return angles_2_and_3


def triangle_calc(num_angles, num_sides, angle_1, angle_2, angle_3, side_1, side_2, side_3):

    if num_angles == 0 and num_sides == 3:
        angle_1_radians = law_of_cosines(side_1, side_2, side_3)

        angles_2_and_3_radians = law_of_sines_1_angle_3_sides(angle_1_radians, side_1, side_2, side_3)
        all_angles = [angle_1_radians, angles_2_and_3_radians[0], angles_2_and_3_radians[1]]
        all_angles_degrees = [degrees(angle_1_radians), degrees(angles_2_and_3_radians[0]),
                              degrees(angles_2_and_3_radians[1])]
        print(all_angles)
        print(all_angles_degrees)


triangle_calc(num_angles=0, num_sides=3, angle_1=None, angle_2=None, angle_3=None,
              side_1=20, side_2=50, side_3=60)
