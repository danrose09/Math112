from math import cos, sin, acos, asin, pi


class Point:

    def __init__(self, x_coord, y_coord):
        self._x_coord = x_coord
        self._y_coord = y_coord

    def get_x_coord(self):
        return self._x_coord

    def get_y_coord(self):
        return self._y_coord


class Circle:

    def __init__(self, radius, coordinates, theta):
        self._radius = radius
        self._coordinates = coordinates
        self._theta = theta
        self._arclength = None
        self._cosine_x = None
        self._sine_y = None
        self._tan = None
        self._arccos = None
        self._arcsin = None

    def get_radius(self):
        return self._radius

    def get_theta(self):
        # if self._theta is None:
        #     self._theta = float(input("If theta is known, please input now: "))
        #     return self._theta
        # else:
        return self._theta

    def get_coordinates(self):
        return self._coordinates.get_x_coord(), self._coordinates.get_y_coord()

    def get_arclength(self):
        self._arclength = self._theta*self._radius
        return self._arclength, round(self._arclength*self._radius, 6)

    def get_cos_x(self):
        self._cosine_x = cos(self._theta)
        return self._cosine_x, self._cosine_x*self._radius

    def get_sin_y(self):
        self._sine_y = sin(self._theta)
        return self._sine_y, self._sine_y * self._radius

    def get_tan(self):
        self._tan = self._coordinates.get_y_coord() / self._coordinates.get_x_coord()
        return self._tan

    def get_arccos_x(self):
        x_coord_in_radians = self._coordinates.get_x_coord() / self._radius
        print(x_coord_in_radians)
        self._arccos = round(acos(x_coord_in_radians), 6)
        return self._arccos

    def get_arcsin_y(self):
        y_coord_in_radians = self._coordinates.get_y_coord() / self._radius
        print(y_coord_in_radians)
        self._arcsin = round(acos(y_coord_in_radians), 6)
        return self._arcsin

    def set_theta(self):
        self._theta = self._arclength / self._radius
        return self._theta


my_coordinates = Point(1.3, 2)
new_circle = Circle(2.6, my_coordinates, theta=2.35619)

# print(new_circle.get_arclength())
print(new_circle.get_arcsin_y())

