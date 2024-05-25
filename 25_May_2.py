"""In a college programming competition, participants are given a task to process a list of an integer array. For each integer, they must compute and print the product of its digits.

Your task is to assist them with the program.

Input format:

The first line of input consists of an integer N, representing the number of elements in the array.

The second line consists of N space-separated integers, representing the array elements.

Output format:

The output displays the product of digits for N integers, separated by a space."""

def product_of_digits(num):
    product = 1
    while num > 0:
        digit = num % 10
        product *= digit
        num //= 10
    return product

def main():
    # Read the number of elements in the array
    N = int(input())
    # Read the array elements
    arr = list(map(int, input().split()))
    
    # List to store the product of digits for each element
    products = []
    
    # Compute the product of digits for each element
    for num in arr:
        products.append(product_of_digits(abs(num)))  # Use abs(num) to handle negative numbers correctly
    
    # Print the products separated by a space
    print(' '.join(map(str, products)))

if __name__ == "__main__":
    main()
