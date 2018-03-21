#!/usr/bin/env python
print "Content-Type: text/html"
print
print ''' <link href="https://fonts.googleapis.com/css?family=Open+Sans&amp;subset=cyrillic-ext" rel="stylesheet">   <meta charset="UTF-8">
<link rel="stylesheet" href="/Rotator/styles.css"> '''
print '<title>Settings</title>'

import cgi
import os
import Cookie
import mysql.connector

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
  except KeyError:
    print '<h1>Are you logged in?</h1>'
    print ' <meta http-equiv="refresh" content="3;url=/Rotator/login.html" />  '
#end of that section 

dataField = cgi.FieldStorage()
try:
  global name
  name = "\'" + dataField.getvalue("name") + "\'"
  global email
  email = "\'" + dataField.getvalue("email") + "\'"
except:
  print "<h1>You can only leave the phone field empty!</h1><meta http-equiv=\"refresh\" content=\"3;url=/Rotator/settings.html\" />"
  quit()
  
connection = mysql.connector.connect(
  user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
  )

cursor = connection.cursor(buffered = True)
phone = dataField.getvalue("phone")
if( phone == None or phone == ""):
  cursor.execute("UPDATE User SET Name = %s, Email = %s, Phone = NULL WHERE ID = %s" % (name, email, userId) )
else:
  cursor.execute("UPDATE User SET Name = %s, Email = %s, Phone = %s WHERE ID = %s" % (name, email, phone, userId) )
connection.commit()

#probably we should have some HTML here or just close the tab ???

cursor.close()
connection.close()

print "<h1>Your settings were changed successfully!</h1><meta http-equiv=\"refresh\" content=\"3;url=/Rotator/cgi-bin/settings.cgi\" />"
