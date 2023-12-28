def main():
    total = 0
    while True:
        try:
            item_price = round(float(menu[input("Item: ").title()]), 2)
            #print("{0:.2f}".format(item_price))
            total += item_price
            print("Total: ", "${0:.2f}".format(total))
        except KeyError:
            pass
        except EOFError:
            print("\n")
            break


menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

main()
