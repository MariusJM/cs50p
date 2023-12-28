def main():
    date = get_input("Date: ")
    date_cleaned = clean_date(date)
    date_splittet = date_cleaned.split()
    month_replaced = replace_month(date_splittet[0], months)
    print(
        f"{int(date_splittet[2]):02}",
        "-",
        f"{int(month_replaced):02}",
        "-",
        f"{int(date_splittet[1]):02}",
        sep="",
        end="",
    )


months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def replace_month(month, list):
    if month in list:
        return list.index(month) + 1
    else:
        return month


def clean_date(x):
    cleaned = ""
    for i in str(x):
        if i.isalnum():
            cleaned += i
        else:
            cleaned += " "
    return cleaned


def get_input(x):
    while True:
        try:
            i = input(x)
            date = clean_date(i).split()
            if date[1].isalpha():
                pass
            elif not date[0].isalpha() and int(date[0]) > 12:
                pass
            elif int(date[1]) > 30:
                pass
            else:
                return i
        except EOFError:
            return
        except ValueError:
            pass


main()
