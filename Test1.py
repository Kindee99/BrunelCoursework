c = input("Enter today/'s date (dd/mm/yyyy)")
if(c[2] =="/" and c[5]=="/"):
    c = c.split('/')
    day = int(c[0])
    month = int(c[1])
    year = int(c[2])
    if(month >= 1 and month <= 13 and len(str(year)) == 4):
        if(month == 1):
            month = "Jan"
        elif(month == 2):
            month = "Feb"
        elif(month == 3):
            month = "March"
        elif(month == 4):
            month = "Apr"
        elif month == 5:
            month = "May"
        elif month == 6:
            month = "Jun"
        elif month == 7:
            month = "Jul"
        elif month == 8:
            month = "Aug"
        elif month == 9:
            month = "Sep"
        elif month == 10:
            month = "Oct"
        elif month == 11:
            month = "Nov"
        elif month == 12:
            month = "Dec"
        full_Date = str(day) + " " + str(month) + " " + str(year)
        print("Today/'s date is " + str(full_Date))
    else:
        print("invalid input")
else:
    print("invalid input")