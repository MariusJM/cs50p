import sys
import csv

def main():
    cla_i, cla_o = check_cla()
    items = []

    try:
        with open(cla_i, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        sys.exit(f"Could not read {cla_i}")

def check_cla():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        print(sys.argv[1], sys.argv[2])
        return (sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
