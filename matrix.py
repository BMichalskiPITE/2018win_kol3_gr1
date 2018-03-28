class Matrix:
    def __init__(self, *args):
        if len(args) % 2 != 0:
            raise ValueError("Invalid number of arguments!")

        self._n = len(args) // 2
        self._values = args[:]


    def __str__(self):
        return str(self._values)


    def size(self):
        return self._n


    def add(self, matrix):
        if self.size() != matrix.size():
            raise ValueError("Sizes must be equal. Left matrix size = {}, "
                             "right matrix size = {}.".format(self.size(), matrix.size()))
        result_values = []
        for a, b in zip(self._values, matrix._values):
            result_values.append(a + b)

        return Matrix(tuple(result_values))
