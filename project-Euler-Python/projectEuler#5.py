# HackerRank Project Euler #5
# Smallest multiple evenly divisible by all numbers 1..N

import math

def smallest_multiple(n):
    lcm = 1
    for i in range(1, n + 1):
        lcm = lcm * i // math.gcd(lcm, i)
    return lcm

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(smallest_multiple(N))
