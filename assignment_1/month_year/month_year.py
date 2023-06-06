""" print the calender for given month and year"""
import calendar

# Get year from the user
YEAR = int(input("Enter the year:"))

# Get month from the user
MONTH = int(input("Enter the month in digits:"))

# Print the calendar for the specified year and month
print(calendar.month(YEAR, MONTH))
