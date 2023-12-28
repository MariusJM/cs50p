import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time = re.search(r"^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)?$", s, re.IGNORECASE)
    if not time:
        raise ValueError

    first_hour = f"{int(time.group(1)):02}"
    first_minutes = ""
    second_hour = f"{int(time.group(4)):02}"
    second_minutes = ""


    if time.group(1) == "12" and time.group(3) == "AM":
        first_hour = "00"
    elif time.group(3) == "PM":
        first_hour = int(first_hour) + 12

    if time.group(2) == None:
        first_minutes = "00"
    elif int(time.group(2)) >= 60:
        raise ValueError
    else:
        first_minutes = f"{time.group(2):02}"

    if time.group(4) == "12" and time.group(6) == "PM":
        second_hour = "12"
    elif time.group(6) == "PM":
        second_hour = int(second_hour) + 12

    if time.group(5) == None:
        second_minutes = "00"
    elif int(time.group(5)) >= 60:
        raise ValueError
    else:
        second_minutes = f"{time.group(5):02}"



    return(f'{first_hour}:{first_minutes} to {second_hour}:{second_minutes}')


...


if __name__ == "__main__":
    main()
