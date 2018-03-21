#!/usr/bin/env python
print "Content-Type: text/html"
print
print ''' <link href="https://fonts.googleapis.com/css?family=Open+Sans&amp;subset=cyrillic-ext" rel="stylesheet">   <meta charset="UTF-8">
<link rel="stylesheet" href="/Rotator/styles.css"> '''

import cgi
import mysql.connector

dataField = cgi.FieldStorage()

userId = dataField.getvalue('userID')

connection = mysql.connector.connect(
  user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
  )

cursor = connection.cursor(buffered = True)

cursor.execute("DELETE FROM User_Group_Log WHERE User_ID = %s" % (userId) )
connection.commit()
cursor.close()
connection.close()

print "<h1>User removed</h1><meta http-equiv=\"refresh\" content=\"3;url=/Rotator/cgi-bin/settings.cgi\" /> "
