def main():

    due_amount = 50
    while due_amount > 0:
        print("Amount Due:", due_amount)
        coin = int(input("Insert Coin:"))
        if coin_check(coin) == True:
            due_amount = due_amount - coin
    print("Change Owed:", abs(due_amount))



def coin_check(i):
    if i == 25 or i == 10 or i == 5:
        return True
    else:
        return False
main()
