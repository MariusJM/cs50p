def main():
    name = input("Greeting: ").strip().lower().split(None, 1)[0]
    print("$" + check(name))

def check(x):
    if x == str("hello") or x == str("hello,"):
        return str(0)
    elif x.find("h") == 0:
        return str(20)
    else:
        return str(100)

main()
