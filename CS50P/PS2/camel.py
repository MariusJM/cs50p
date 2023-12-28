
def main():
    camelCase = input("camelCase: ")
    print("snake_case:", snake_case(camelCase))

def snake_case(phrase):
    snake = ""
    for i in range(len(phrase)):
        if phrase[i].isupper():
            snake = snake + "_" + phrase[i].lower()
        else:
            snake = snake + phrase[i]
    return snake

main()
