from datetime import date

def print_current_date():
    # Read the current date
    current_date = date.today()

    # Print the formatted date
    print("Today is : %d-%d-%d" % (current_date.day,current_date.month,current_date.year))

    # Set the custom date
    custom_date = date(2020, 12, 16)
    print("The date is:",custom_date)

if __name__ == '__main__':
    print_current_date()