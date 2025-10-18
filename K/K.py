import sys

def divisibility():
    m = int(sys.stdin.readline().strip())
    n = sys.stdin.readline().strip()

    sum_of_digits = sum(int(digit) for digit in n)

    if sum_of_digits % (m - 1) == 0:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    divisibility()

