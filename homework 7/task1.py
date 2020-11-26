class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        text = ""
        for line in self.matrix:
            text += " ".join([str(i) for i in line])
            text += "\n"
        return text

    def __add__(self, other):
        new_matrix = []
        for row in range(len(self.matrix)):
            line = []
            for column in range(len(self.matrix[0])):
                line.append(self.matrix[row][column] + other.matrix[row][column])
            new_matrix.append(line)
        return Matrix(new_matrix)


matrix = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
e = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print(matrix+e)
