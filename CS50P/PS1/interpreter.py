def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    print(doMath(x,y,z))

def doMath(x,y,z):
    if y == "+":
        return round(float(x) + float(z), 1)
    elif y == "-":
        return round(float(x) - float(z), 1)
    elif y == "*":
        return round(float(x) * float(z), 1)
    elif y == "/":
        return round(float(x) / float(z), 1)

main()
