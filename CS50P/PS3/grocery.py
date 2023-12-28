def main():
    item = get_input()


def get_input():
    while True:
        try:
            x = input().upper()
#            print("getInput", x)
            store_input(x)
        except EOFError:
            #print("\n")
            item_list_sorted = dict(sorted(item_list.items()))
            for key, value in item_list_sorted.items():
                print(value, key)
            break

item_list = {}

def store_input(x):
    if x not in item_list:
        item_list[x] = 1
        #print("NOT IN THE LIST")
    else:
        item_list[x] += 1
        #print("item in the list", item_list[x])

main()
