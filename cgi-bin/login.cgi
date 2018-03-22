#!/usr/bin/env python

import mysql.connector
import bcrypt
import cgi
import datetime

dataField = cgi.FieldStorage()
try:
  global username
  username = "\"" + dataField.getvalue('username') + "\""
  global password
  password = dataField.getvalue('password')
except:
  print "Content-Type: text/html\n\n"
  print "'<link rel=\"stylesheet\" href=\"/Rotator/styles.css\">'<TITLE>Login</TITLE><h1>You can't leave empty fields!</h1><meta http-equiv=\"refresh\" content=\"5;url=/Rotator/login.html\" />"
  quit()
  

connection = mysql.connector.connect(
    user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
    )

cursor= connection.cursor()
try:
  cursor.execute("SELECT Password_Hash, ID FROM User WHERE Username = %s " % (username) )
  global table
  table =  cursor.fetchall()[0]
except:
  print "Content-Type: text/html\n\n"
  print "'<link rel=\"stylesheet\" href=\"../styles.css\">'<TITLE>Login</TITLE><h1>Wrong login!</h1><meta http-equiv=\"refresh\" content=\"5;url=/Rotator/login.html\" />"
  quit()

hashed = table[0]
userId = table[1]
if bcrypt.checkpw(password, hashed):
  import Cookie
  c = Cookie.SimpleCookie()
  c['Rotator'] = userId
  c['Rotator']['expires'] = (datetime.datetime.now() + datetime.timedelta(minutes= 30) ).ctime()
  print c
  print "Content-Type: text/html\n\n"
  print """
'<link rel="stylesheet" href="../styles.css">'
"<TITLE>Login</TITLE>"
"<H1>Login page</H1>"
    <head> 
      <meta http-equiv="refresh" content="0;url=./timetable.cgi" /> 
      <h1>You are going to be redirected</h1> 
  </head> 
  """
else:
  print "Content-Type: text/html\n\n"
  print "<h1>Wrong password!</h1>"
  print """
  '<link rel="stylesheet" href="/Rotator/styles.css">'
"<TITLE>Login</TITLE>"
    <head> 
      <meta http-equiv="refresh" content="5;url=/Rotator/login.html" /> 
  </head> 
  """
  


cursor.close()
connection.close()
