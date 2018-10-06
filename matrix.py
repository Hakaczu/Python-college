class Matrix:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.values = []

    def insert(self):
        self.values = [0] * self.rows
        for i in range(self.rows):
            self.values[i] = [0] * self.columns
        for i in range(0, int(self.rows)):
            for j in range(0, int(self.columns)):
                self.values[i][j] = int(input("Insert " + str(i+1) + "x" + str(j+1) + " value: "))

    def add(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            return "Columns or rows are not the same"
        else:
            new_matrix = [[self.values[i][j] + other.values[i][j] for j in range(self.rows)] for i in
                          range(self.columns)]
            return new_matrix

    def subtract(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            return "Columns or rows are not the same"
        else:
            new_matrix = [[self.values[i][j] - other.values[i][j] for j in range(self.rows)] for i in
                          range(self.columns)]
            return new_matrix

    def multiply(self, other):
        if self.columns != other.rows:
            return "The columns of the first matrix are not the same as the rows of the second matrix"
        else:
            new_matrix = [0] * self.rows
            for i in range(self.rows):
                new_matrix[i] = [0] * other.columns
            for i in range(0, self.rows):
                for j in range(0, other.columns):
                    for ij in range(0, self.columns):
                        new_matrix[i][j] += self.values[i][ij] * other.values[ij][j]
            return new_matrix
# TO DO Determinant //PL: nie jestem pewny o co wyznacznika dlatego go zostawiłem.

    def determinant(self, mul):
        if self.columns == self.rows:
            size = self.rows
            new_matrix = []
            delta = size
            for row in self.values:
                new_row = []
                for v in range(2 * size - 1):
                    new_row.append(row[v - delta])
                new_matrix.append(new_row)
            new_matrix = Matrix(*new_matrix)
            result = 0
            size = new_matrix.rows
            delta = 0
            for i in range(size):
                temp = 1
                for j in range(size):
                    temp *= new_matrix.values[i + j - delta][i + j]
                delta += 1
                result += temp
            delta = 0
            for i in reversed(range(size)):
                temp = 1
                for j in range(size):
                    temp *= new_matrix.values[i - j - delta][i - j]
                delta += 1
                result -= temp
            return result
        else:
            raise Exception("To calculate determinant of the matrix "
                            "size of column and row should be the same")
