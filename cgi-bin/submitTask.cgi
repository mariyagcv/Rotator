#!/usr/bin/env python
print "Content-Type: text/html"
print 
print ''' <link href="https://fonts.googleapis.com/css?family=Open+Sans&amp;subset=cyrillic-ext" rel="stylesheet">   <meta charset="UTF-8">
<link rel="stylesheet" href="/Rotator/styles.css"> '''

import cgi
import Cookie
import os
from datetime import datetime
import mysql.connector
#from emailResponses import mailResponseToSubmit

#check for cookie and use it assign user ID - should be everywhere at the beggining!
if not 'HTTP_COOKIE' in os.environ:
  print '<h1>Are you logged in?</h1>'
  print ' <meta http-equiv="refresh" content="3;url=/Rotator/login.html" />  '
else:
  c = Cookie.SimpleCookie()
  c.load(os.environ.get('HTTP_COOKIE'))
  
  try:
    global userId
    userId = c['Rotator'].value
    print "<TITLE>Submit Task</TITLE>"
  except KeyError:
    print '<h1>Are you logged in?</h1>'
    print ' <meta http-equiv="refresh" content="3;url=/Rotator/login.html" />  '
#end of that section 

dataField = cgi.FieldStorage()

connection = mysql.connector.connect(
  user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
  )
cursor = connection.cursor(buffered = True)


#mailResponseToSubmit(userId)
cursor.execute("UPDATE User_Task_Log SET Submitted = 1, Submitted_Date = %s WHERE Submitted = 0 AND User_ID = %s AND Deadline = %s AND Task_ID = %s" % ("\'" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\'", userId, "\'" + dataField.getvalue("deadline") + "\'", dataField.getvalue("task_id")) )
#kill the connection to DB
connection.commit()
cursor.close()
connection.close()
print '<h1>Redirecting...</h1>'
print '<meta http-equiv="refresh" content="0;url=/Rotator/cgi-bin/timetable.cgi"/> '
