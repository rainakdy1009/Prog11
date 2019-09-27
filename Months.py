month = input("Enter a month: ")
if month == "April" or month == "June" \
   or month == "September" or month == "November" :
    print("There are 30 days in this month")

if month == "January" or month == "March" \
   or month == "May" or month == "July" or month == "August" \
   or month == "October" or month == "December" :
    print("There are 31 days in this month")

if month == "February" :
    print("There are 28 or 29 days in this month")
