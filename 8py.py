def fibonacci_recursive(n):
    if n <= 0:
        return "Input must be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Generate first 10 numbers
n_terms = 10
print(f"Fibonacci sequence ({n_terms} terms):")
for i in range(1, n_terms + 1):
    print(fibonacci_recursive(i), end=" ")
print()
