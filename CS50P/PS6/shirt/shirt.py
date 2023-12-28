import sys
import os
from PIL import Image, ImageOps

def main():
    cla_input, cla_output = check_cla()
    try:
        with Image.open(cla_input) as user_input, Image.open("shirt.png") as shirt:
            user_input = ImageOps.fit(user_input, shirt.size)
            user_input.paste(shirt, box=None, mask=shirt)
            user_input.save(cla_output)
    except FileNotFoundError:
        sys.exit("Input does not exist")


def check_cla():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif str(os.path.splitext(sys.argv[1])[1]).lower() != str(os.path.splitext(sys.argv[2])[1]).lower():
        sys.exit("Input and output have different extensions")
    elif str(os.path.splitext(sys.argv[1])[1]).lower() != ".png" and str(os.path.splitext(sys.argv[1])[1]).lower() != ".jpg":
        sys.exit("Invalid output")
    else:
        return sys.argv[1], sys.argv[2]


if __name__ == "__main__":
    main()
