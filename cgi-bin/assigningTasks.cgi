#!/usr/bin/env python

import mysql.connector
import cgi
import os
import Cookie
from assigningTasksWeekly import query


print "Content-Type: text/html"
print
print '''
<link href="https://fonts.googleapis.com/css?family=Open+Sans&amp;subset=cyrillic-ext" rel="stylesheet">   <meta charset="UTF-8">
<link rel="stylesheet" href="../styles.css"> 
'''

#check for cookie and use it assign user ID - should be everywhere at the beggining!
if not 'HTTP_COOKIE' in os.environ:
  print '<h1>Are you logged in?</h1>'
  print ' <meta http-equiv="refresh" content="3;url=../login.html" />  '
else:
  c = Cookie.SimpleCookie()
  c.load(os.environ.get('HTTP_COOKIE'))
  
  try:
    print '<TITLE> Assigning the tasks...</TITLE>'
    global userId
    userId = c['Rotator'].value
  except KeyError:
    print '<h1>Are you logged in?</h1>'
    print ' <meta http-equiv="refresh" content="3;url=../login.html" />  '
#end of that section 

connection = mysql.connector.connect(
  user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
  )

cursor = connection.cursor(buffered = True)
cursor.execute("SELECT Group_ID FROM User_Group_Log WHERE User_ID = %s" % userId)
if len(cursor.fetchall()) == 0:
  print "<h2>There are no tasks to assign. Make sure you've added tasks to your group! </h2>"
else:
  groupId = cursor.fetchall()[0]
  query(userId, groupId)
  print "<h2>New tasks where added to your schedule!<h2>"
#kill the connection to DB
cursor.close()
connection.close()

print '''
<meta http-equiv="refresh" content="3;url=./timetable.cgi" /> 
'''



