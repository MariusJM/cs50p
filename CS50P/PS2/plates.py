def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not is_numeric(s):
        return False
    elif len(s) < 2 or len(s) > 6:
        return False
    elif first_number(s):
        return False
    elif letters_after(s):
        return False
    else:
        return True

def is_numeric(s):
    return s.isalnum()

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



main()
