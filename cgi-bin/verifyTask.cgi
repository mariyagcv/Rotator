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
    print "<TITLE>RotatoR</TITLE>"
  except KeyError:
    print '<h1>Are you logged in?</h1>'
    print ' <meta http-equiv="refresh" content="3;url=/Rotator/login.html" />  '
    quit()
#end of that section 

dataField = cgi.FieldStorage()

connection = mysql.connector.connect(
  user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
  )

cursor.execute("SELECT User_ID FROM User_Task_Log WHERE Submitted_Date = %s" % ("\'" + dataField.getvalue('submitteddate') + "\'")
if cursor.fetchall()[0][0] == userId:
  print '''
  <h1> You can't verify your own task! </h1>
  '''
  quit()
else:
  cursor = connection.cursor(buffered = True)
  cursor.execute("UPDATE User_Task_Log SET Verified = 1, Verified_Date = %s WHERE ID = %s" % (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), userTaskId) )
  #kill the connection to DB
  connection.commit()
  cursor.close()
  connection.close()

print '<meta http-equiv="refresh" content="5;url=/Rotator/cgi-bin/newsfeed.cgi" />'#HTML to redirect here <3
