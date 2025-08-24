# HackerRank Project Euler #2
# Sum of even Fibonacci numbers <= N

import math
import os
import random
import re
import sys

def even_fib_sum(n):
    a, b = 1, 2
    total = 0
    while b <= n:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    return total

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input("input:"))
        print(even_fib_sum(N))