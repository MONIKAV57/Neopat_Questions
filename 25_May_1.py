"""Akar is working on a program that modifies a given matrix based on the presence of zeros in its rows and columns.

He needs your help to write a program that takes an input matrix and modifies it as follows: if a cell in the matrix contains a zero, then the entire row and column of that cell should be set to zero. I

Assist him by writing the program.

Input format:

The first line consists of two integers rand c, separated by a space, representing the number of rows and columns in the matrix.

The next r lines contain c space-separated integers, representing the elements of the matrix.

Output format:

If there are zeros in the matrix, display the modified matrix after replacing rows and columns with zeros if any element in the row or column is zero. If there are no zeros in the matrix, display the given matrix as it is.
    """
    
def set_zeros(matrix, r, c):
    # Step 1: Initialize sets to keep track of rows and columns to be zeroed
    zero_rows = set()
    zero_columns = set()
    
    # Step 2: Identify all rows and columns that contain zeros
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_columns.add(j)
    
    # Step 3: Modify the matrix
    # Set the identified rows to zero
    for row in zero_rows:
        for j in range(c):
            matrix[row][j] = 0
    
    # Set the identified columns to zero
    for col in zero_columns:
        for i in range(r):
            matrix[i][col] = 0
    
    return matrix

def main():
    # Read input for the number of rows and columns
    r, c = map(int, input().split())
    
    # Read the matrix
    matrix = []
    for _ in range(r):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    # Modify the matrix based on zeros
    modified_matrix = set_zeros(matrix, r, c)
    
    # Print the modified matrix
    for row in modified_matrix:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()
