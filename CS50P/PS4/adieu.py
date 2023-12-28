def main():
    get_input()


name_list = []
counter = 0


def get_input():
    while True:
        try:
            x = input()
            store_input(x)
        except EOFError:
            # print("\n")
            adieu(name_list)
            break


def store_input(x):
    name_list.append(x)


def adieu(x):
    counter = 0
    final_output = "Adieu, adieu, to"
    if len(x) == 1:
        print(final_output, x[0])
    elif len(x) == 2:
        print(final_output, x[0], "and", x[1])
    else:
        while counter < len(x[:-1]):
            final_output += f" {x[counter]},"
            counter += 1
        final_output += f" and {x[counter]}"
        print(final_output)


main()
