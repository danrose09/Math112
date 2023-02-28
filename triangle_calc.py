from math import sin, cos, acos, radians, degrees


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



def triangle_calc(num_angles, num_sides, angle_1, angle_2, angle_3, side_1, side_2, side_3):

    if num_angles == 0 and num_sides == 3:
        angle_1_radians = law_of_cosines(side_1, side_2, side_3)

        law_of_sines_1_angle_3_sides(angle_1_radians, side_1, side_2, side_3)


triangle_calc(num_angles=0, num_sides=3, angle_1=None, angle_2=None, angle_3=None,
              side_1=20, side_2=50, side_3=60)
