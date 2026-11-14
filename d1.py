
# Recursive Fibonacci
def recursive(n):
    if n <= 1:
        return n
    return recursive(n-1) + recursive(n-2)


# Non-Recursive Fibonacci
def non_recursive(n):
    a, b = 0, 1

    for i in range(n):
        print(a)
        a, b = b, a + b


n = int(input("Enter number of terms: "))

print("\nRecursive Fibonacci:")
for i in range(n):
    print(recursive(i))

print("\nNon-Recursive Fibonacci:")
non_recursive(n)


# Time and Space Complexity:

# Recursive Method:
# Time Complexity: O(2^n)
# Space Complexity: O(n)

# Non-Recursive Method:
# Time Complexity: O(n)
# Space Complexity: O(1)
