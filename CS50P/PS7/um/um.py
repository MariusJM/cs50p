import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    um = re.findall(r"\b(um\b)", s, re.IGNORECASE)
    return len(um)


if __name__ == "__main__":
    main()
