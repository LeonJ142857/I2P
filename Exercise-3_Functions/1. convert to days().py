def get_days(hours, minutes, seconds):
    days = round(float((hours*3600+minutes*60+seconds)/(24*3600)),4)
    print("The number of days is:", days)


def convert_to_days():
    hours = int(input("Enter number of hours: "))
    minutes = int(input("Enter number of minutes: "))
    seconds = int(input("Enter number of seconds: "))
    get_days(hours, minutes, seconds)
