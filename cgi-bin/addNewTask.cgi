#!/usr/bin/env python
print "Content-Type: text/html"
print
print ''' <link href="https://fonts.googleapis.com/css?family=Open+Sans&amp;subset=cyrillic-ext" rel="stylesheet">   <meta charset="UTF-8">
<link rel="stylesheet" href="/Rotator/styles.css"> '''
print '<title>Settings</title>'
import cgi
import Cookie
import os
from datetime import datetime
import mysql.connector
import random

#check for cookie and use it assign user ID - should be everywhere at the beggining!
if not 'HTTP_COOKIE' in os.environ:
  print '<h1>Are you logged in?</h1>'
  print ' <meta http-equiv="refresh" content="3;url=/Rotator/login.html" />  '
  quit()
else:
  c = Cookie.SimpleCookie()
  c.load(os.environ.get('HTTP_COOKIE'))
  
  try:
    global userId
    userId = c['Rotator'].value
  except KeyError:
    print '<h1>Are you logged in?</h1>'
    print ' <meta http-equiv="refresh" content="3;url=/Rotator/login.html" />  '
    quit()
#end of that section 

dataField = cgi.FieldStorage()

try:
  global name
  name = "\'" + dataField.getvalue("taskName") + "\'"
  global difficulty
  difficulty = int(dataField.getvalue("taskDiff"))
except:
  print '''<h1>The format you provided is invalid:</h1><h3> task name must be a non-empty string and difficulty must be a valid integer</h3><meta http-equiv="refresh" content="5;url=/Rotator/cgi-bin/settings.cgi" />'''
  quit()

connection = mysql.connector.connect(
  user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
  )

cursor = connection.cursor(buffered=True)

cursor.execute("SELECT Group_ID FROM User_Group_Log WHERE User_ID = %s" % (userId) )

groupId = cursor.fetchall()[0][0]

randomId = random.randint(1, 8388607)
try:
  cursor.execute("SELECT ID FROM User WHERE ID = %s" % randomId)
  while(cursor.rowcount != 0):
    randomId = random.randint(1, 8388607)
    cursor.execute("SELECT ID FROM User WHERE ID = %s" % randomId)
except Exception:
  pass
  
cursor.execute("INSERT INTO Task(ID, Name, Difficulty, Group_ID) VALUES (%s, %s, %s, %s)" % (randomId, name, difficulty, groupId) )
connection.commit()
cursor.close()
connection.close()

print '<h1>The new task has been added!</h1><meta http-equiv="refresh" content="3;url=/Rotator/cgi-bin/settings.cgi" /> '
