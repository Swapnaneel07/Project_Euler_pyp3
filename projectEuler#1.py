#Problem 1: Multiples of 3 and 5

import math
import os
import random
import re
import sys

def sum_of_multiples(k, n):
    m = (n - 1) // k
    return k * m * (m + 1) // 2

def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    T = int(input_data[0])
    results = []
    for i in range(1, T + 1):
        N = int(input_data[i])
        total = sum_of_multiples(3, N) + sum_of_multiples(5, N) - sum_of_multiples(15, N)
        results.append(str(total))
    print("\n".join(results))


if __name__ == "__main__":
    solve()
