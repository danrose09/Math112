from math import cos, sin


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

    def get_radius(self):
        return self._radius

    def get_theta(self):
        return self._theta

    def get_coordinates(self):
        return self._coordinates.get_x_coord(), self._coordinates.get_y_coord()

    def get_arclength(self):
        self._arclength = self._theta*self._radius
        return self._arclength, round(self._arclength*self._radius, 6)

    def get_cos_x(self):
        self._cosine_x = cos(self._coordinates.get_x_coord())
        return self._cosine_x, self._cosine_x*self._radius

    def set_theta(self):
        self._theta = self._arclength / self._radius
        return self._theta


my_coordinates = Point(1.3, 2)
new_circle = Circle(2.6, my_coordinates, theta=0.789)

print(new_circle.get_arclength())
print(new_circle.get_cos_x())

