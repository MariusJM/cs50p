def main():
    time = input("What time is it? ")
    timeComverted = convert(time)
    if 7.0 <= timeComverted <=8.0:
        print("breakfast time")
    elif 12.0 <= timeComverted <= 13.0:
        print("lunch time")
    elif 18.0 <= timeComverted <= 19.0:
        print("dinner time")



def convert(time):
    hours, minutes = time.split(":")
    if int(minutes) != 0:
        minutes = 1/(60/int(minutes))
        return int(hours) + minutes
    else:
        return float(hours)



if __name__ == "__main__":
    main()
