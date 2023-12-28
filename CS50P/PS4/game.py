import random


while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
        else:
            pass
    except ValueError:
        pass
    except NameError:
        pass
    except IndexError:
        pass

answer = random.randint(1, level)


while True:
    try:
        guess = int(input("Guess: "))
        if guess < answer:
            print("Too small!")
        elif guess > answer:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        pass
    except NameError:
        pass
