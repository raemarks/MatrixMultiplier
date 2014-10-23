import sys
class MatrixMultiplier:
        # Multiplies given matrices if compatible
        def multiply(self, m1, m2):
                # Check if both are matrices
                if not (self.check_matrix_type(m1) and
                                self.check_matrix_type(m2)):
                        return None
                # Check if number of rows in first is same as number of columns
                # in second
                if len(m1[0]) != len(m2):
                        return None
                nrows = len(m1)
                ncols = len(m2[0])
                # Make empty matrix
                res = self.make_new_matrix(nrows, ncols)
                # Multiply rows and columns to build
                for x in range(nrows):
                        for y in range(ncols):
                                res[x][y] = self.mul_row_col(m1, m2, x, y)
                return res

        # Checks if it's a matrix: list of lists with all rows having same
        # length
        # TODO: make sure all items are numbers
        def check_matrix_type(self, matrix):
                if type(matrix) is not list:
                        return False
                if len(matrix) == 0:
                        return False
                if type(matrix[0]) is not list:
                        return False
                row_len = len(matrix[0])
                for row in matrix:
                        if type(row) is not list:
                                return False
                        elif len(row) is not row_len:
                                return False
                return True

        # Makes a zero'd matrix of the specified size
        def make_new_matrix(self, row, col):
                matrix = []
                for i in range(row):
                        new_row = []
                        for i in range(col):
                                new_row.append(0)
                        matrix.append(new_row)
                return matrix

        # Multiplies one row by one column
        def mul_row_col(self, m1, m2, row, col):
                res = 0
                for i in range(len(m2)):
                        res += m1[row][i] * m2[i][col]
                return res

        # Pretty-prints the matrix
        # TODO: make it print-format so adding more digits doesn't shift matrix
        def print_matrix(self, matrix):
                for row in matrix:
                        sys.stdout.write('[ ')
                        for col in row:
                                sys.stdout.write(str(col) + ' ')
                        print(']')


def main():
        mm = MatrixMultiplier()
        mm.print_matrix(mm.multiply([[1,2,3],[4,5,6]], [[7,8],[9,10],[11,12]]))
        mm.print_matrix(mm.multiply([[1, 0], [1, 1]], [[1, 0], [1,1]]))

if __name__ == "__main__":
        main()
