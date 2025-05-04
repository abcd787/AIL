# Non AI Magic Square
def is_magic_square(matrix):
    size = len(matrix)

    # Check if it's a square matrix
    for row in matrix:
        if len(row) != size:
            return False

    # Calculate the sum of the first diagonal (top-left to bottom-right)
    main_diagonal_sum = 0
    for i in range(size):
        main_diagonal_sum += matrix[i][i]

    # Calculate the sum of the second diagonal (top-right to bottom-left)
    other_diagonal_sum = 0
    for i in range(size):
        other_diagonal_sum += matrix[i][size - i - 1]

    # Check if diagonals are equal
    if main_diagonal_sum != other_diagonal_sum:
        return False

    # Check rows and columns
    for i in range(size):
        row_sum = sum(matrix[i])
        column_sum = 0
        for j in range(size):
            column_sum += matrix[j][i]

        if row_sum != main_diagonal_sum or column_sum != main_diagonal_sum:
            return False

    return True


# Main program
size = int(input("Enter size of square matrix (e.g., 3 for 3x3): "))
print("Enter the matrix row by row (space-separated numbers):")

matrix = []
for i in range(size):
    row_input = input(f"Row {i+1}: ").split()
    row = [int(num) for num in row_input]
    matrix.append(row)

# Check and print result
if is_magic_square(matrix):
    print("Magic Square")
else:
    print("Not a Magic Square")
