import sys
import pyfiglet


def main():
    fonts = pyfiglet.FigletFont.getFonts()

    if check_cla(sys.argv) == True:
        if len(sys.argv)> 1:
            check_font(sys.argv[2], fonts)
            user_text = input()
            print(pyfiglet.figlet_format(user_text, font = sys.argv[2]))
        else:
            user_text = input()
            print(pyfiglet.figlet_format(user_text))

def check_font(x, y):
    if x in y:
        return True
    else:
        sys.exit(1)


def check_cla(x):
    if len(x) == 1:
        return True
    elif len(x) == 3:
        if "-f" in x[1:] or "--font" in x[1:]:
            return True
        else:
            sys.exit(1)
    else:
        print("Invalid usage")
        sys.exit(1)


main()
