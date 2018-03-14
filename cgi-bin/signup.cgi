#!/usr/bin/env python

print "Content-Type: text/html"
print
print "<TITLE> Signup </TITLE>"
print "<H1>Redirecting...</H1>"

import bcrypt
import cgi
import mysql.connector
import random


dataField = cgi.FieldStorage()

password = dataField.getvalue("password")[0]
password = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

connection = mysql.connector.connect(
    user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
    )

cursor= connection.cursor(buffered = True)

randomId = random.randint(1, 8388607)
try:
  cursor.execute("SELECT ID FROM User WHERE ID = %s" % randomId)
  while(cursor.rowcount != 0):
    randomId = random.randint(1, 8388607)
    cursor.execute("SELECT ID FROM User WHERE ID = %s" % randomId)
except Exception:
  pass
  
cursor.execute("""
INSERT INTO User (ID, Name, Username, Password_Hash, Email)
VALUES (%s, %s, %s, %s, %s) 
""" % (randomId, "\"" + dataField.getvalue("name") + "\"", "\"" + dataField.getvalue("username") + "\"" ,"\"" + password + "\"", "\"" + dataField.getvalue("email") + "\"") )

connection.commit()
cursor.close()
connection.close()

print """
  <head> 
    <meta http-equiv="refresh" content="5;url=../timetable.html" /> 
    <title>You are going to be redirected</title> 
</head> 
"""

#some HTML here probably ^^
