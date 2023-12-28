import sys

def main():
    python_file = check_argument()
    try:
        with open(python_file) as file:
            counter = 0
            for line in file:
                if line.strip().startswith("#") or line == "\n" or line.strip() == "":
                    continue
                else:
                    counter += 1
        print(counter, end="")
    except FileNotFoundError:
        sys.exit("File does not exist")


def check_argument():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif sys.argv[1][-3:] != ".py":
        sys.exit("Not a Python file")
    else:
        return sys.argv[1]


if __name__ == "__main__":
    main()
