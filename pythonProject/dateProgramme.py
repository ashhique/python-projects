import datetime
now = datetime.datetime.now()
day = input("Enter today's day (1 to 31): ")
month = input("Enter month (1 to 12): ")
year = input("Enter year: ")
endings = ["st","nd","rd",] + 17 * ["th"] + ["st","nd","rd",] + 7 * ["th"] + ["st"]
endingIndex = int(day)-1
dayOutput = day + endings[endingIndex]
monthName = ["january", "february","march","april","may","june","july","August", "September", "October", "november","December"]
monthIndex = int(month)-1
monthOutput = monthName[monthIndex]
print(dayOutput+ " " + monthOutput + ", " + year)
end = datetime.datetime.now()
diff = end - now
print(diff)

