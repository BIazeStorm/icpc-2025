import sys
from collections import defaultdict

def circle_arena():
    try:
        r_str = sys.stdin.readline().strip()
        if not r_str: return
        r = int(r_str)

        n = int(sys.stdin.readline().strip())

        distance_counts = defaultdict(int)

        for _ in range(n):
            x, y = map(int, sys.stdin.readline().strip().split())

            dist_sq = x*x + y*y
            distance_counts[dist_sq] += 1

        total_balanced_pairs = 0

        for k in distance_counts.values():
            if k > 1:
                pairs_in_group = k * (k - 1) // 2
                total_balanced_pairs += pairs_in_group

        print(total_balanced_pairs)

    except (IOError, ValueError):
        return


if __name__ == "__main__":
    circle_arena()
