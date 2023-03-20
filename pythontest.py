import django
#import requests
#import os
#import sys
import datetime
import cgi

def get_current_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


print(django.__version__)
print (get_current_time())

#!/usr/bin/env python3

form = cgi.FieldStorage()
name = form.getvalue("name")

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Greeting</title>")
print("</head>")
print("<body>")
print("<h1>Hello, " + name + "!</h1>")
print("</body>")
print("</html>")
