#!/usr/bin/env python
print "Content-Type: text/html"
print
print ''' <link href="https://fonts.googleapis.com/css?family=Open+Sans&amp;subset=cyrillic-ext" rel="stylesheet">   <meta charset="UTF-8">
<link rel="stylesheet" href="/Rotator/styles.css"> '''

import cgi
import Cookie
import os
import mysql.connector

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

taskName = "\'" + dataField.getvalue('taskName') + "\'"
taskDiff = int(dataField.getvalue('taskDiff'))

connection = mysql.connector.connect(
  user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
  )

cursor = connection.cursor(buffered = True)

cursor.execute("SELECT Group_ID FROM User_Group_Log WHERE User_ID = %s" % (userId) )

groupId = cursor.fetchall()[0][0]

cursor.execute("DELETE FROM Task WHERE Group_ID = %s AND Name = %s AND Difficulty = %s" % (groupId, taskName, taskDiff) )
connection.commit()
cursor.close()
connection.close()

print "<h1>Task removed</h1><meta http-equiv=\"refresh\" content=\"3;url=/Rotator/cgi-bin/settings.cgi\" /> "
