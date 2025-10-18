import sys

def card_focus():
        cards = sys.stdin.readline().strip()

        parts = cards.split()

        cards_quantity = int(parts[0])
        black_left = int(parts[1])

        print(black_left)

if __name__ == "__main__":
    card_focus()
