#!/usr/bin/env python
import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
textText = form.getvalue("example1")

print("Content-Type:text/html\n\n")
print(textText)
