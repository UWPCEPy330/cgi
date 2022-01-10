#!/usr/bin/env python3
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
listval = form.getlist('operand')



try: 
    sum = 0
    for i in listval:
        sum += int(i)

    body = "The sum is: " + i
except (ValueError, TypeError):
    body = "Unable to calculate, please provide valid operands."

print("Content-type: text/plain")
print()
print(body)
