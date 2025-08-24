# HackerRank Project Euler #4
# Largest palindrome product of two 3-digit numbers ≤ N

def largest_palindrome(n):
    max_pal = -1
    for i in range(100, 1000):
        for j in range(i, 1000):
            prod = i * j
            if prod <= n and str(prod) == str(prod)[::-1]:
                max_pal = max(max_pal, prod)
    return max_pal

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(largest_palindrome(N))
