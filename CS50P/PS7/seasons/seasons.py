from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    try:
        year, month, day = input("Date of Birth:").split("-")
    except ValueError:
        sys.exit("Invalid date")


    print(convert_time(year, month, day))



def convert_time(year, month, day):
    time_passed = date.today() - date(int(year), int(month), int(day))
    minutes = int(time_passed.total_seconds()/60)
    output = p.number_to_words(minutes, andword="") + " minutes"
    return output.capitalize()


if __name__ == "__main__":
    main()
