#!/usr/bin/env python
print "Content-Type: text/html"
print
print '''
<TITLE> Task details</TITLE>
<link href="https://fonts.googleapis.com/css?family=Open+Sans&amp;subset=cyrillic-ext" rel="stylesheet">   <meta charset="UTF-8">
<link rel="stylesheet" href="../styles.css"> 
'''
import cgi
import Cookie
import mysql.connector
import os

dataField = cgi.FieldStorage()

#check for cookie and use it assign user ID - should be everywhere at the beggining!
if not 'HTTP_COOKIE' in os.environ:
  print '<h1>Are you logged in?</h1>'
  quit()
else:
  c = Cookie.SimpleCookie()
  c.load(os.environ.get('HTTP_COOKIE'))
  try:
    global userId
    userId = c['Rotator'].value
  except KeyError:
    print '<h1>Are you logged in?</h1>'
    quit()
#end of that section 

print '''
<h1> %s </h1> <br>
<h2>Deadline:  %s</h2> <br>
<h2>Difficulty:  %s </h2><br>
<input type="button" value="Close this window" onclick="self.close()">
''' % (dataField.getvalue('name'), dataField.getvalue('deadline'), dataField.getvalue('difficulty') )
print '''
<input type="button" value="Submit" onclick="window.location.href='/Rotator/cgi-bin/submitTask.cgi?task_id=%s&deadline=%s' ">
''' % (dataField.getvalue('task_id'), dataField.getvalue('deadline') )
