def main():
    name = str(input("Greeting: ").strip().lower().split(None, 1)[0])
    print("$" + str(value(name)))
    exit(1)


def value(x):
    if x == str("hello") or x == str("hello,") or x == str("Hello") or x == str("Hello,"):
        return int(0)
    elif x.find("h") == 0 or x.find("H") == 0:
        return int(20)
    else:
        return int(100)




if __name__ == "__main__":
    main()
