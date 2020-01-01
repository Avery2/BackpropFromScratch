# Matrix objects
# Operations


class Matrix:
    def __init__(self, height=0, width=0):
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @width.setter
    def set_width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            raise ValueError("please enter a digit")  # unsure of terminology

    @height.setter
    def set_height(self, value):
        if value.isdigit():
            self.__height = value
        else:
            raise ValueError("please enter a digit")  # unsure of terminology


my_matrix = Matrix(5, 5)
print(f"height {my_matrix.height} width {my_matrix.width}")
