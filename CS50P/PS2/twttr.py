def main():
    user_input = input("Input: ")
    output = ""
    for i in str(user_input):
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            output = output
        else:
            output = output + i
    print(output)

main()
