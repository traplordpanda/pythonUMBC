#!/usr/bin/env python3
import cgi
fields = cgi.FieldStorage()
default = ""
first_name = fields.getvalue("first_name", default)
last_name = fields.getvalue("last_name", default)
comments = fields.getvalue("comments", default)
# This is the Head of the HTTP response
print("Content-type: text/html\n")

# This begins the Body of the HTTP Response
print("<html><head><title>Thank You</title></head>")
print("<body>")
print("<h1>Thank you",  first_name, last_name, "</h1>")
print("Your comments below are greatly appreciated<br>")
print("<em>", comments, "</em>")
print("</body></html>")
