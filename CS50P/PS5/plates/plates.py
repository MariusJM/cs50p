def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #print(len(s), len(s) < 2)

    if is_numeric(s):
        return False
    elif len(str(s)) < 2:
        #print("Check short length")
        return False
    elif len(s) > 6:
        #print("Check long length")
        return False
    elif s[0].isnumeric():
        return False
    elif s[1].isnumeric():
        return False
    elif first_number(s):
        return False
    elif letters_after(s):
        return False
    elif not is_alnumeric(s):
        return False
    else:
        return True

def is_alnumeric(s):
    return s.isalnum()

def is_numeric(s):
    return s.isnumeric()

def first_number(s):
    number_detected = 0
    for i in s:
        if i.isnumeric():
            number_detected += 1
            if i == "0" and number_detected == 1:
                return True

def letters_after(s):
    number_detected = 0
    for i in s:
        if i.isnumeric():
            number_detected += 1
        elif i.isalpha() and number_detected > 0:
            return True


if __name__ == "__main__":
    main()
