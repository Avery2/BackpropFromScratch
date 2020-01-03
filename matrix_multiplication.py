# Matrix objects
# Operations


class Matrix:
    def __init__(self, rows: int = 0, columns: int = 0, values=None):
        if values is None:
            values = []
            self._rows = rows
            self._columns = columns
        self._values = values
        if not values:  # if empty list (the default value; an empty list is implicitly false)
            print(type(rows))
            for x in range(0, rows):
                values.append([])
                for y in range(0, columns):
                    # print(f"({x}, {y})")
                    values[x].append(0)
        # need to iterate through to make sure dimensions are correct (ie they are filled - and if not fill with zeros?)
        self._rows = len(values)
        self._columns = len(values[0])

    @property
    def values(self):
        return self._values

    @property
    def rows(self):
        return self._rows

    @property
    def columns(self):
        return self._columns

    def column(self, num):
        # need to transpose
        my_column = []
        for x in self._values:
            my_column.append(x[num])  # this'll probably break with 1D matrices
        return my_column

    def row(self, num):
        return self._values[num]

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


def matmul(a: Matrix, b: Matrix):
    # dimensions of a matrix: row x columns
    # In order for matrix multiplication to be defined, the number of columns in the first matrix must be equal to the
    # number of rows in the second matrix.
    product = []
    if a.columns != b.rows:
        raise ValueError("dimensions incorrect, product is undefined")
    # product dimensions will be rows_of_a by columns_of_b
    for x in range(0, a.rows):
        product.append([])  # prob break for 1D array
        for y in range(0, b.columns):
            product[x].append(dot(a.row(x), b.column(y)))
    return product  # filler, not functional


def dot(a: list, b: list):
    # dot product returns a single value from two equal length sequences
    if len(a) != len(b):
        raise ValueError("dot product needs equal length sequences")
    dot_product = 0
    for i in range(0, len(a)):
        dot_product += a[i] * b[i]
    return dot_product

# test_values = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# my_matrix = Matrix(5, 5, test_values)
# mat_a = Matrix(5, 5)
# mat_b = Matrix(5, 5)
# print("a")
# print(f"rows {mat_a.rows} columns {mat_a.columns}")
# print(mat_a.values)
#
# print("b")
# print(f"rows {mat_b.rows} columns {mat_b.columns}")
# print(mat_b.values)
#
# print("a x b")
# print(matmul(mat_b, mat_b))
