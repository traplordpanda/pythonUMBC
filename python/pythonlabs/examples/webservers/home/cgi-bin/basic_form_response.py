#!/usr/bin/env python3
import cgi
import calendar
import time

# This is the Head of the HTTP response
print("Content-type: text/html\n")

# This begins the Body of the HTTP Response
print("<html><head><title>A Basic Response</title></head>")
print("<body>")
print("<h1>Welcome</h1>")
print("<h4>Today is: ", time.ctime(), "</h4>")
print("<hr>")
cal = calendar.HTMLCalendar(firstweekday=calendar.SUNDAY)
print(cal.formatmonth(2017, 5, withyear=True))
print("</body></html>")
