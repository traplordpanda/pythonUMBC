#!/usr/bin/env python3
import cgi
import os

# This is the Head of the HTTP response
print("Content-type: text/html\n")

# This begins the Body of hte HTTP Response
print("<html><head><title>CGI Environment</title></head>")
print("<body>")
print("<h1>Environment</h1>")
print("<dl>")
keys = list(os.environ.keys())
keys.sort()
for key in keys:
    print("<dt><strong>", key, "</strong></dt>", sep="")
    print("<dd><em>", os.environ[key], "</em></dd>", sep="")
print("</dl>")
print("</body></html>")
