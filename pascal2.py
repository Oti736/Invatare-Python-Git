#Pascal's Triangle problem solved with Combinations
#Pascal's triangle works for combinations because each entry in the triangle represents a combination, specifically "n choose k" {}_{n}C_{k}, where n is the row number and k is the position in that row, both starting from zero. The triangle's construction method, where each number is the sum of the two above it, directly corresponds to the fundamental combination identity.
import math

def factorial(n):
   "We calculate the factorial of a number."
return math.factorial(n)

def combinations(n, k):
    " We apply the formula of (C_n^k). "
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1

return factorial(n) // (factorial(k) * factorial(n - k))

def pascal_triangle_comb(num_rows):
    "We generate Pascal's Triangle with Combinations "
    triangle = []
    for n in range(num_rows):
        num_rows = []
        # in the n row we have n+1 elements, from k=0 to k=n
        for k in range(n + 1):
            value = combinations(n, k)
            num_rows.append(value)
        triangle.append(num_rows)

return triangle

# Example 
N = 10
result = pascal_triangle_comb(N)

# Print the triangle
print(f"Pascal's Triangle (with C(n, k)) for {N} rows:")
for row in result:
    print(row)
