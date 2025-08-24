# HackerRank Project Euler #6
# Difference between square of sums and sum of squares

def sum_square_diff(n):
    sum_sq = n * (n + 1) * (2*n + 1) // 6
    sq_sum = (n * (n + 1) // 2) ** 2
    return sq_sum - sum_sq

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(sum_square_diff(N))
