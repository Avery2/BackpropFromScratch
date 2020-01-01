# Matrix objects
# Operations


class Matrix:
    def __init__(self, height=0, width=0, values=None):
        if values is None:
            values = []
        self._values = values
        self._height = height
        self._width = width
        if not values:  # if empty list (the default value; an empty list is implicitly false)
            for x in range(0, height):
                values.append([])
                for y in range(0, width):
                    print(f"({x}, {y})")
                    values[x].append(0)
        # need to iterate through to make sure dimensions are correct

    @property
    def values(self):
        return self._values

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value.isdigit():
            self._width = value
        else:
            raise ValueError("please enter a digit")  # unsure of terminology

    @height.setter
    def height(self, value):
        if value.isdigit():
            self._height = value
        else:
            raise ValueError("please enter a digit")  # unsure of terminology


test_values = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# my_matrix = Matrix(5, 5, test_values)
my_matrix = Matrix(5, 5)
print(f"height {my_matrix.height} width {my_matrix.width}")
print(my_matrix.values)
