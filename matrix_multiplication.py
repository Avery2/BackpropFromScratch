# Matrix objects
# Operations


class Matrix:
    def __init__(self, height=0, width=0, values=[]):
        self._values = values
        self._height = height
        self._width = width
        for x in range(0, height):
            values.append([])
            for y in range(0, width):
                print(f"({x}, {y})")
                values[x].append(0)

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
    def set_width(self, value):
        if value.isdigit():
            self._width = value
        else:
            raise ValueError("please enter a digit")  # unsure of terminology

    @height.setter
    def set_height(self, value):
        if value.isdigit():
            self._height = value
        else:
            raise ValueError("please enter a digit")  # unsure of terminology


my_matrix = Matrix(5, 5)
print(f"height {my_matrix.height} width {my_matrix.width}")
print(my_matrix.values)
