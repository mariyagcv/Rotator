#!/usr/bin/env python
print "Content-Type: text/html"
print
print ''' <link href="https://fonts.googleapis.com/css?family=Open+Sans&amp;subset=cyrillic-ext" rel="stylesheet">   <meta charset="UTF-8">
<link rel="stylesheet" href="/Rotator/styles.css"> '''

import cgi
import Cookie
import os
from datetime import datetime, timedelta
import mysql.connector
from rotator import LongerTask


#check for cookie and use it assign user ID - should be everywhere at the beggining!
if not 'HTTP_COOKIE' in os.environ:
  print '<h1>Are you logged in?</h1>'
  print ' <meta http-equiv="refresh" content="3;url=../login.html" />  '
else:
  c = Cookie.SimpleCookie()
  c.load(os.environ.get('HTTP_COOKIE'))
  
  try:
    global userId
    userId = c['Rotator'].value
    print "<TITLE>RotatoR</TITLE>"
  except KeyError:
    print '<h1>Are you logged in?</h1>'
    print ' <meta http-equiv="refresh" content="3;url=../login.html" />  '
#end of that section 


connection = mysql.connector.connect(
  user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
  )

cursor = connection.cursor(buffered = True)
cursor.execute("SELECT Task_ID, Deadline, Submitted, Submitted_Date, Verified, Verified_Date FROM User_Task_Log WHERE User_ID = %s" % (userId) )
output = cursor.fetchall()

tasks = []

for element in output:
  cursor.execute("SELECT Name, Difficulty FROM Task WHERE ID = %s" %(element[0]))
  output2 = cursor.fetchall()[0]
  task = LongerTask(str(element[0]), str(output2[0]), output2[1], str(element[1]), str(element[2]), str(element[3]), str(element[4]), str(element[5]) )
  tasks.append(task)


cursor.close()
connection.close()

mondayTask = []
tuesdayTask = []
wednesdayTask = []
thursdayTask = []
fridayTask = []
satMorTask = []
satEveTask = []
sunMorTask = []
sunEveTask = []

for task in tasks:
  deadline = datetime.strptime(task.deadline, "%Y-%m-%d %H:%M:%S")
  if deadline.weekday() == 0:
    mondayTask.append(task)
  elif deadline.weekday() == 1:
    tuesdayTask.append(task)
  elif deadline.weekday() == 2:
    wednesdayTask.append(task)
  elif deadline.weekday() == 3:
    thursdayTask.append(task)
  elif deadline.weekday() == 4:
    fridayTask.append(task)
  elif deadline.weekday() == 5:
      if deadline.hour == 12:
        satMorTask.append(task)
      else:
        satEveTask.append(task)
  elif deadline.weekday() == 6:
      if deadline.hour == 12:
        sunMorTask.append(task)
      else:
        sunEveTask.append(task)

display = '''

<html>

<body class = "inside" id="uberbar">
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

<body class = "inside">
  <div class = "centeredTimeTable">

  <h1>YOUR SCHEDULE</h1> <!-- WHY ISJN'T ROTATOR RESPONSIVE !??? -->


<!-- BTW TIMETABLE IS NOT YET RESPONSIVE AND LOOKS SHIT ON PHONES
     BUT TRY TO FIX LATER ON -->
  <table>
  <tr>
    <th class = "weekDays">Weekday</th>
    <th class = "weekDays">Morning task</th>
    <th class = "weekDays">Evening task</th>
  </tr>

  <tr>
    <td class = "weekDays">Monday</td>
    <td class = "noTask">No task</td>
    <td class = '''
if(len(mondayTask) == 0):
  addition = ' "noTask">No task'
else:
  addition = ' "task"> '
  for task in mondayTask:
    addition += task.name + "<br>"
display += addition +'''</td>
  </tr>
  <tr>
    <td class = "weekDays">Tuesday</td>
    <td class = "noTask">No task</td>
    <td class = '''
if(len(tuesdayTask) == 0):
  addition = ' "noTask">No task'
else:
  addition = ' "task"> '
  for task in tuesdayTask:
    addition += task.name + "<br>"
display += addition +'''</td>
  </tr>
  <tr>
    <td class = "weekDays">Wednesday</td>
    <td class = "noTask">No task</td>
    <td class = '''
if(len(wednesdayTask) == 0):
  addition = ' "noTask">No task'
else:
  addition = ' "task"> '
  for task in wednesdayTask:
    addition += task.name + "<br>"
display += addition +'''</td>
  </tr>
  <tr>
    <td class = "weekDays">Thursday</td>
    <td class = "noTask">No task</td>
    <td class = '''
if(len(thursdayTask) == 0):
  addition = ' "noTask">No task'
else:
  addition = ' "task"> '
  for task in thursdayTask:
    addition += task.name + "<br>"
display += addition +'''</td>
  </tr>
  <tr>
    <td class = "weekDays">Friday</td>
    <td class = "noTask">No task</td>
    <td class = '''
if(len(thursdayTask) == 0):
  addition = ' "noTask">No task'
else:
  addition = ' "task"> '
  for task in thursdayTask:
    addition += task.name + "<br>"
display += addition +'''</td>
  </tr>
  <tr>
    <td class = "weekDays">Saturday</td>
    <td class = '''
if(len(satMorTask) == 0):
  addition = ' "noTask">No task'
else:
  addition = ' "task"> '
  for task in satMorTask:
    addition += task.name + "<br>"
display += addition +'''</td>
    <td class = '''
if(len(satEveTask) == 0):
  addition = ' "noTask">No task'
else:
  addition = ' "task"> '
  for task in satEveTask:
    addition += task.name + "<br>"
display += addition +'''</td>
  </tr>
  <tr>
    <td class = "weekDays">Sunday</td>
    <td class = '''
if(len(sunMorTask) == 0):
  addition = ' "noTask">No task'
else:
  addition = ' "task"> '
  for task in sunMorTask:
    addition += task.name + "<br>"
display += addition +'''</td>
    <td class = '''
if(len(sunEveTask) == 0):
  addition = ' "noTask">No task'
else:
  addition = ' "task"> '
  for task in sunEveTask:
    addition += task.name + "<br>"
display += addition +'''</td>
  </tr>

  </table>



</div>
</body>
</div>
</html>
'''

print display

