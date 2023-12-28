import sys
import csv

def main():
    cla_i, cla_o = check_cla()
    items = []

    try:
        with open(cla_i) as file:
            reader = csv.DictReader(file)

            for row in reader:
                second, first = row["name"].split(", ")
                house = row["house"]
                items.append({"first": first, "last": second, "house": house})

        with open(cla_o, "w") as output:
            fieldnames=["first", "last", "house"]
            writer = csv.DictWriter(output, fieldnames)
            writer.writeheader()
            for row in items:
                name = row["first"]
                last_name = row["last"]
                address = row["house"]
                writer.writerow({"first": name, "last": last_name, "house": address})


    except FileNotFoundError:
        sys.exit(f"Could not read {cla_i}")


def check_cla():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        return (sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
