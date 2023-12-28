def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            break
        except(ValueError, ZeroDivisionError):
            continue
    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split("/")
    if int(x) > int(y) or x.isdigit() == False or y.isdigit() == False:
        raise ValueError
    elif int(y) == 0:
        raise ZeroDivisionError
    else:
        return round(int(x)/int(y)*100)



def gauge(percentage):
    if percentage < 2:
        return "E"
    elif percentage > 98:
        return "F"
    elif percentage >100:
        return
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
