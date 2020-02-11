"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

# Error Handling, throws on ValueError
def use():
    print('Usage: 14_cal.py [month?: int] [year? int]')
    sys.exit()

def main():
    read = sys.argv
    today = datetime.now()
    month = calendar.month

    try:
        if len(read) == 1:
            print(month(today.year, today.month))
        if len(read) == 2:
            print(month(today.year, int(read[1])))
        if len(read) >= 3:
            print(month(int(read[2]), int(read[1])))
    # Errors out if input cannot be cast into a number
    except:
        use()

if __name__ == "__main__":
    main()
