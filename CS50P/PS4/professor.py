import random


def main():
    level = get_level()
    correct_answers = 0

    for i in range(9):
        incorect_ansers = 3
        x = generate_integer(level)
        y = generate_integer(level)
        z = x + y
        correct_answers += answer(x, y, z)
    print(correct_answers)


def answer(x, y, z):
    count = 2
    while True:
        try:
            user_input = int(input((f"{x} + {y} = ")))
            if user_input == z:
                return 1
            elif count > 0:
                print("EEE")
                count -= 1
            else:
                print(f"{x} + {y} = {z}")
                return 0
        except TypeError:
            pass
        except ValueError:
            pass


def get_level():
    while True:
        try:
            x = int(input("Level: "))
            if 0 < x < 4:
                return x
            else:
                pass
        except TypeError:
            pass
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        upperLimit = (10 * level) - 1
        return random.randint(0, upperLimit)
    elif level == 2:
        upperLimit = (10**level) - 1
        return random.randint(10, upperLimit)
    else:
        upperLimit = (10**level) - 1
        return random.randint(100, upperLimit)


if __name__ == "__main__":
    main()
