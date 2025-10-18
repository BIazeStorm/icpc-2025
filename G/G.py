import sys
import math

def elliptical_arena():
    try:
        n, m = map(int, sys.stdin.readline().strip().split())
    except ValueError:
        return

    if n > m:
        n, m = m, n

    total_points = 2 * m + 1

    for i in range(1, n + 1):
        numerator = m**2 * (n**2 - i**2)
        denominator = n**2

        j_max = math.isqrt(numerator // denominator)

        points_in_column = 2 * j_max + 1

        total_points += 2 * points_in_column

    print(total_points)


if __name__ == "__main__":
    elliptical_arena()
