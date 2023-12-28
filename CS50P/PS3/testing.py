"""
def main():
    x = number_split(user_input("Fraction: "))
    y = x[0]
    z = x[1]

    while True:
        try:
            if int(y)>int(z):
                break
            print(round(100/int(z)*int(y)), "%", sep="")
            break
        except ZeroDivisionError:
            break


def user_input(x):
    return input(x)


def number_split(x):
    return (x.split("/"))

main()
"""
def main():
    d = {'A':110, 'a':100, 'T':50, 't':5}
    from collections import Counter
    c = Counter()
    for k,v in d.items():
        c.update({k.upper(): v})
        print()


main()
