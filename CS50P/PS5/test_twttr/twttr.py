def main():
    word = str(input("Input: "))
    print(shorten(word))

def shorten(word):
    output = ""
    for i in str(word):
        if i == "a" or i == "A" or i == "e" or i == "E" or i == "i" or i == "I" or  i == "o" or i == "O" or i == "u" or i == "U":
            output = output
        else:
            output = output + i
    return(output)


if __name__ == "__main__":
    main()
