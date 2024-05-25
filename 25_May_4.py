"""Rohit is working on a new programming challenge. He needs to write a program that reads a matrix of integers and prints its elements in a special zigzag pattern. The zigzag pattern alternates between printing the elements of each row from left to right and from right to left.

Help Rohit by writing a program that reads a matrix of integers, prints its elements in the desired zigzag pattern, and then outputs the result.

Input format:

The first line of input consists of two space-separated integers m and n, representing the order of the matrix.

The next m lines consist of n space-separated integers, representing the elements of the matrix.

Output format:

The output prints space-separated integers, representing the elements of the matrix in the zigzag pattern."""
def print_zigzag(matrix, m, n):
    result = []
    
    for i in range(m):
        if i % 2 == 0:
            # Print the row left to right
            result.extend(matrix[i])
        else:
            # Print the row right to left
            result.extend(matrix[i][::-1])
    
    print(' '.join(map(str, result)))

def main():
    # Read the dimensions of the matrix
    m, n = map(int, input().split())
    
    # Read the matrix
    matrix = []
    for _ in range(m):
        row = list(map(int, input().split()))
        matrix.append(row)
    
    # Print the matrix in zigzag pattern
    print_zigzag(matrix, m, n)

if __name__ == "__main__":
    main()
