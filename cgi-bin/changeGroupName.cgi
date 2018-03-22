#!/usr/bin/env python

print "Content-Type: text/html"
print
print "<TITLE> Settings </TITLE>"
print ''' <link href="https://fonts.googleapis.com/css?family=Open+Sans&amp;subset=cyrillic-ext" rel="stylesheet">   <meta charset="UTF-8">
<link rel="stylesheet" href="/Rotator/styles.css"> '''

import cgi
import os
import Cookie
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

groupName = "\'" + dataField.getvalue('groupName') + "\'"

connection = mysql.connector.connect(
  user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
  )

cursor = connection.cursor(buffered=True)

cursor.execute("SELECT Group_ID FROM User_Group_Log WHERE User_ID = %s" % (userId) )

groupId = cursor.fetchall()[0][0]

cursor.execute("UPDATE WorkGroup SET Name = %s WHERE ID = %s" %(groupName, groupId) )

connection.commit()
cursor.close()
connection.close()

print '<h1>The group name has been changed!</h1><meta http-equiv="refresh" content="3;url=/Rotator/cgi-bin/settings.cgi" /> '
