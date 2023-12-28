def main():
    while True:
        try:
            x = number_split(user_input("Fraction: "))
            y = x[0]
            z = x[1]
            percent = round(100/int(z)*int(y))
            if int(y)>int(z):
                pass
            elif int(percent) < 2:
                print("E")
                break
            elif int(percent) > 98:
                print("F")
                break
            elif int(percent) >100:
                break
            print(round(100/int(z)*int(y)), "%", sep="")
            break
        except ZeroDivisionError:
            pass
        except ValueError:
            pass
        except IndexError:
            pass


def user_input(x):
    return input(x)


def number_split(x):
    return (x.split("/"))

main()
