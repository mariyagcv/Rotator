#!/usr/bin/env python
print "Content-Type: text/html"
print
print ''' <link href="https://fonts.googleapis.com/css?family=Open+Sans&amp;subset=cyrillic-ext" rel="stylesheet">   <meta charset="UTF-8">
<link rel="stylesheet" href="/Rotator/styles.css"> '''

import cgi
import Cookie
import os
import mysql.connector
from datetime import datetime

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
    print "<TITLE>News Feed</TITLE>"
  except KeyError:
    print '<h1>Are you logged in?</h1>'
    print ' <meta http-equiv="refresh" content="3;url=/Rotator/login.html" />  '
    quit()
#end of that section 

connection = mysql.connector.connect(
  user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
  )

cursor = connection.cursor(buffered = True)

try:
  cursor.execute("SELECT Group_ID FROM User_Group_Log WHERE User_ID = %s" % (userId) )
  group_Id = cursor.fetchall()[0][0]
  cursor.execute("SELECT User_ID FROM User_Group_Log WHERE Group_ID = %s" % (group_Id) )
  userIds = cursor.fetchall() # ((userId), (userId)...)
except:
  print '<h1>You are not in any group!</h1> <meta http-equiv="refresh" content="3;url=/Rotator/group.html" />'
  quit()



users = []

for user in userIds:
  cursor.execute("SELECT ID, Name FROM User WHERE ID = %s" % (user[0]) )
  fetched = cursor.fetchall()[0]
  users.append((fetched[0], fetched[1]))
  # (id, name)

cursor.execute("SELECT ID, Name, Difficulty FROM Task WHERE Group_ID = %s" % (group_Id) )

tasks = cursor.fetchall() # tasks contains now tuples in form (id, name, diff)
if len(tasks) == 0:
  print '<h1> Your group has no tasks assingned to it!</h1><meta http-equiv="refresh" content="3;url=/Rotator/cgi-bin/settings.cgi" />'
  quit()

userTaskLogs = []

for i in range(0, len(users) ):
  try:
    cursor.execute("SELECT Deadline, Submitted, Submitted_Date, Verified, Verified_Date, User_ID, Task_ID FROM User_Task_Log WHERE User_ID = %s" % (users[i][0]) )
    fetched = cursor.fetchall()[0]
    userTaskLogs.append((fetched, users[i][1]) )
  except:
    pass
  # ((deadline, sub, sub_date, ver, ver_date, uID, tID), uName) (...)

html = '''
<html>

<script src="/Rotator/menuScript.js"></script>
<div id="mySidenav" class="sidenav">
  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
  <a href="/Rotator/cgi-bin/timetable.cgi">Timetable</a>
  <a href="/Rotator/cgi-bin/newsfeed.cgi">Newsfeed</a>
  <a href="/Rotator/cgi-bin/settings.cgi">Settings</a>
  <a href="/Rotator/about.html">About</a>
  <a href="/Rotator/cgi-bin/logout.cgi">Log out</a>
</div>
<div id="rest">
  <span onclick="openNav()">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <div class="menu-icon">
      <a href="#" class="btn"><i class="fa fa-bars"></i></a>
    </div>
  </span>
<body class="inside">
  <h1 class = "taskClass">News Feed</h1>
  <div class = "tasks"> '''
newsfeed =[]
for userTaskLog in userTaskLogs:
  #for loop to find the name of the task
  taskName = "TASK NAME NOT FOUND"
  for task in tasks:
    if task[0] == userTaskLog[0][6]:
      taskName = task[1]
      break
  if userTaskLog[0][0] < datetime.now(): # deadline passed
    if userTaskLog[0][1] == 0 or userTaskLog[0][0] < userTaskLog[0][2]: #failed
      newsfeed.append(('%s missed the deadline for %s on %s' % (userTaskLog[1], taskName, userTaskLog[0][0]), userTaskLog[0][0]))
      # (string, datetime)
    else: # submition before deadline
      if userTaskLog[0][3] == 0: # not verified yet
        newsfeed.append(('%s finished the task %s on %s. Please verify it by the end of the week! <br> <input type="button" style = "background: #00b33c;padding: 12px 20px; margin: 8px 0; color: white;border: 1px solid #ccc;   border-radius: 4px; box-sizing: border-box; font-size: 13px; " value="Verify" onclick="window.location.href=\'/Rotator/cgi-bin/verifyTask.cgi?submitteddate=%s\' ">' % (userTaskLog[1], taskName, userTaskLog[0][2], userTaskLog[0][2]), userTaskLog[0][2]))
      else: #verified
        newsfeed.append(('%s had finished the task %s on %s and it was verified on %s' % (userTaskLog[1], taskName, userTaskLog[0][2], userTaskLog[0][4]), userTaskLog[0][4] ))    
  else: # deadline is still up
    if userTaskLog[0][1] == 1:
      if userTaskLog[0][3] == 0: # not verified yet
        newsfeed.append(('%s finished the task %s on %s. Please verify it by the end of the week! <br> <input type="button" style = "background: #00b33c; padding: 12px 20px; margin: 8px 0; color: white;border: 1px solid #ccc;   border-radius: 4px; box-sizing: border-box; font-size: 13px; " value="Verify" onclick="window.location.href=\'/Rotator/cgi-bin/verifyTask.cgi?submitteddate=%s\' ">' % (userTaskLog[1], taskName, userTaskLog[0][2], userTaskLog[0][2]), userTaskLog[0][2]))
      else: #verified
        newsfeed.append(('%s had finished the task %s on %s and it was verified on %s' % (userTaskLog[1], taskName, userTaskLog[0][2], userTaskLog[0][4]), userTaskLog[0][4] ))
        
#sort the newsfeed - latest first
for i in range(0, len(newsfeed) - 2):
    for j in range(i, len(newsfeed) - 1):
        if(newsfeed[j][1] < newsfeed[j+1][1]):
            tempNews = newsfeed[j]
            newsfeed[j] = newsfeed[j+1]
            newsfeed[j+1] = tempNews

for news in newsfeed:
  html += '<p class = "taskList">' + news[0] + '</p>'
  
if len(userTaskLogs) == 0:
  html += '<p class = "taskList"> There are no tasks assigned to your group! Run the assignment! </p>'

html += '''
    </div>
</body>
</div>
</html>

'''

print html

cursor.close()
connection.close()
