#!/usr/bin/env python
print "Content-Type: text/html"
print
print ''' <link href="https://fonts.googleapis.com/css?family=Open+Sans&amp;subset=cyrillic-ext" rel="stylesheet">   <meta charset="UTF-8">
<link rel="stylesheet" href="/Rotator/styles.css"> '''

import cgi
import Cookie
import os
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
cursor = connection.cursor(buffered = True)

typeOfGroup = dataField.getvalue('typeOfGroup')

if typeOfGroup == 'new':
  randomId = random.randint(1, 8388607)
  cursor.execute("SELECT ID FROM WorkGroup WHERE ID = %s" % randomId)
  while(cursor.rowcount):
    randomId = random.randint(1, 8388607)
    cursor.execute("SELECT ID FROM WorkGroup WHERE ID = %s" % randomId)
  cursor.execute("INSERT INTO WorkGroup(ID, Name) VALUES (%s, %s)" % (randomId, dataField.getvalue('name') ) )
  groupId = randomId
else:
  groupId = int(dataField.getvalue('groupId') )
  cursor.execute("SELECT ID FROM WorkGroup WHERE ID = %s" % groupId)
  if len(cursor.fetchall() ) == 0:
    print "<h1>Wrong group ID! That group does NOT exist.</h1><meta http-equiv=\"refresh\" content=\"3;url=/Rotator/group.html\" />"
    quit()
  
randomId = random.randint(1, 8388607)
cursor.execute("SELECT ID FROM User_Group_Log WHERE ID = %s" % randomId)
while(cursor.rowcount):
  randomId = random.randint(1, 8388607)
  cursor.execute("SELECT ID FROM User_Group_Log WHERE ID = %s" % randomId)
  
cursor.execute("INSERT INTO User_Group_Log(ID, User_ID, Group_ID) VALUES (%s, %s, %s) " % (randomId, userId, groupId) )
connection.commit()
cursor.close()
connection.close()

print "<h1>You are being redirected...</h1> " # HTML to redirect here
print '<meta http-equiv="refresh" content="3;url=/Rotator/cgi-bin/timetable.cgi" />'
