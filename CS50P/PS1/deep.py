def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    if check_answer(answer) == True:
        print("Yes")
    else:
        print("No")


def check_answer(n):
    if str.lower(n) == str("forty two") or str.lower(n) == str("42") or str.lower(n) == str("forty-two"):
        return True
    else:
        return False

main()
