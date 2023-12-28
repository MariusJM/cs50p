def main():
    print(convert(input()))

def convert(x):
    return x.replace(":)", "\U0001F642").replace(":(", "\U0001F641")

main()