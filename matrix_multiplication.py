# Matrix objects
# Operations


class Matrix:
    def __init__(self, rows=0, columns=0, values=None):
        if values is None:
            values = []
        self._values = values
        self._rows = rows
        self._columns = columns
        if not values:  # if empty list (the default value; an empty list is implicitly false)
            for x in range(0, rows):
                values.append([])
                for y in range(0, columns):
                    # print(f"({x}, {y})")
                    values[x].append(0)
        # need to iterate through to make sure dimensions are correct (ie they are filled - and if not fill with zeros?)

    @property
    def values(self):
        return self._values

    @property
    def rows(self):
        return self._rows

    @property
    def columns(self):
        return self._columns

    @columns.setter
    def columns(self, value):
        if value.isdigit():
            self._columns = value
        else:
            raise ValueError("not a digit")  # unsure of terminology

    @rows.setter
    def rows(self, value):
        if value.isdigit():
            self._rows = value
        else:
            raise ValueError("not a digit")  # unsure of terminology


def matmul(self, a: Matrix, b: Matrix):
    # dimensions of a matrix: row x columns
    # In order for matrix multiplication to be defined, the number of columns in the first matrix must be equal to the
    # number of rows in the second matrix.
    if a.columns != b.rows:
        raise ValueError("dimensions incorrect, product is undefined")
    return a * b  # filler, not functional


test_values = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# my_matrix = Matrix(5, 5, test_values)
a = Matrix(5, 5)
b = Matrix(5, 5)
print("a")
print(f"rows {a.rows} columns {a.columns}")
print(a.values)

print("b")
print(f"rows {b.rows} columns {b.columns}")
print(b.values)

print(matmul(a, b))
