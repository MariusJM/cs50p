import validators
def main():
    email = input("What's your email address?")
    if check_validity(email):
        print("Valid")
    else:
        print("Invalid")


def check_validity(s):
    return validators.email(s)

if __name__ == "__main__":
    main()
