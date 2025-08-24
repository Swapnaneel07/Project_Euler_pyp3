# HackerRank Project Euler #3
# Largest prime factor of N

def largest_prime_factor(n):
    factor = 2
    while factor * factor <= n:
        if n % factor == 0:
            n //= factor
        else:
            factor += 1
    return n

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(largest_prime_factor(N))
