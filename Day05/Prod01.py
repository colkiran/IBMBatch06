
def fact1(n):
    if n < 2:
        return 1
    else:
        return n * fact1(n - 1)

# Example usage
no = 5
print(f"Factorial of {no} is {fact1(no)}")