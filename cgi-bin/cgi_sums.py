#!/usr/bin/env python3
import cgi
import cgitb

cgitb.enable()

form = cgi.FieldStorage()
operands = form.getlist('operand')


total = 0
try: 
    for i in operands:
        total += int(i)

    body = f"Your total is: {total}"
except (ValueError, TypeError):
    body = "Unable to calculate, please provide valid operands."

print("Content-type: text/plain")
print()
print(body)
