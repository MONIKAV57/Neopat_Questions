"""Gokul wants to write a program that takes an array of integers as input and counts the number of unique positive integers present in the array. The program should then output the count of these unique positive integers.

Assist Gokul in creating the program.

Input format:

The first line of input consists of an integer n, representing the number of elements in the array.

The second line consists of n space-separated positive integers.

Output format:

The output prints the count of unique positive integers in the array."""
def main():
    # Read the number of elements in the array
    n = int(input())
    
    # Read the array elements
    arr = list(map(int, input().split()))
    
    # Use a set to store unique positive integers
    unique_positives = set()
    
    # Iterate through the array and add positive integers to the set
    for num in arr:
        if num > 0:
            unique_positives.add(num)
    
    # The number of unique positive integers is the size of the set
    unique_count = len(unique_positives)
    
    # Print the count of unique positive integers
    print(unique_count)

if __name__ == "__main__":
    main()
