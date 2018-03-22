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
  quit()
else:
  c = Cookie.SimpleCookie()
  c.load(os.environ.get('HTTP_COOKIE'))
  
  try:
    global userId
    userId = c['Rotator'].value
  except KeyError:
    print '<h1>Are you logged in?</h1>'
    print ' <meta http-equiv="refresh" content="3;url=../login.html" />  '
    quit()
#end of that section 
connection = mysql.connector.connect(
  user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
  )

cursor = connection.cursor(buffered = True)

cursor.execute("SELECT Name, Email, Phone FROM User WHERE ID = %s" % userId)

details = cursor.fetchall()[0] #details[0] = name, details[1] = email, details[2] = phone

if details[2] == None:
  details = (details[0], details[1], "")

cursor.execute("SELECT WorkGroup.Name, WorkGroup.ID FROM WorkGroup INNER JOIN User_Group_Log ON WorkGroup.ID = User_Group_Log.Group_ID WHERE User_Group_Log.User_ID = %s" % userId )
try:
  groupName = cursor.fetchall()[0] #gname
except:
  groupName = ""

display = '''
<head>
<script src="/Rotator/menuScript.js"></script>
<div id="mySidenav" class="sidenav">
  <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
  <a href="/Rotator/cgi-bin/timetable.cgi">Timetable</a>
  <a href="/Rotator/cgi-bin/newsfeed.cgi">Newsfeed</a>
  <a href="/Rotator/cgi-bin/settings.cgi">Settings</a>
  <a href="/Rotator/about.html">About</a>
  <a href="/Rotator/cgi-bin/logout.cgi">Log out</a>
</div>
</head>
<div id="rest">
  <span onclick="openNav()">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <div class="menu-icon">
      <a href="#" class="btn"><i class="fa fa-bars"></i></a>
    </div>
  </span>
  	</style>

	<link href="https://fonts.googleapis.com/css?family=Open+Sans&amp;subset=cyrillic-ext" rel="stylesheet">   <meta charset="UTF-8">
	  <link rel="stylesheet" href="styles.css">

	<!-- Just tried to add a little title image, I know its not the logo -->
	<link rel="icon" type="image/gif/png" href="logo.png">

	<title>Settings</title>


<body class = "inside">
		<div class="container">
			<h1>Settings</h1><br><br><br><br><br><br><br><br>
			<div class="centered" style="width: 500px; position: relative; margin: 0 0 0 -250px;">
                <br>
                <button type="submit" value="Personal" onclick="document.getElementById('personalSettings').style.display='block'; document.getElementById('groupSettings').style.display='none'; " class = "container1">Personal</button>
                  <div id="personalSettings" style="display: none;">
                  <form action="changeSettings.cgi" method="post">
                    <h3> Your name: </h3><input type="text" name="name" value=%s class = "container1" style="background: white" id = "username">
                    <h3> Your e-mail: </h3><input type="text" name="email" value=%s class = "container1" style="background: white" id = "email">
                    <h3> Your phone: </h3><input type="text" name="phone" value="%s" class = "container1" style="background: white" id = "phone">
                  <button type="submit" value="Save" class = "container1" style="width: 150px;">Save</button>
                  </form>
                  </div>
                <br>
                <button type="submit" value="Submit" onclick="document.getElementById('personalSettings').style.display='none'; document.getElementById('groupSettings').style.display='block'; " class = "container1">Group</button>
                  <div id="groupSettings" style="display: none;"> '''% (details)
if groupName == "":
  display += '''
    <h3> You don't belong to any group! <a href="/Rotator/group.html">Join one now!</a></h3>
  '''
else:
  cursor.execute("SELECT Name, Difficulty FROM Task WHERE Group_ID = %s ORDER BY Difficulty ASC" % (groupName[1]) )
  groupTasks = cursor.fetchall()
  display += '''
              <h3>You want to share your group with others? Give them this number: %s </h3>
                    <form action="changeGroupName.cgi" method="post"> 
                      <h3> Group name: </h3><input type="text" name="groupName" value="%s" class = "container1" style="background: white" id = "groupName">
                  <button type="submit" value="Save" class = "container1" style="width: 150px;">Save</button>
                  </form> 
  <table>
  <tr>
    <th class = "weekDays">ID</th>
    <th class = "weekDays">Difficulty</th>
    <th class = "weekDays">Name</th>
    <th class = "weekDays">Remove</th>
  </tr>
                  ''' % (groupName[1], groupName[0])
  for index in range (0, len(groupTasks)):
    display += '''
  <tr>
    <td class = "weekDays"> %s </td>
    <td class = "task">%s</td>
    <td class = "task">%s</td>
    <td class = "task">
         <form action="removeTask.cgi" method="post"> 
                <input type="text" name="taskName" value=%s class = "container1" style="display: none;">
                <input type="text" name="taskDiff" value=%s class = "container1" style="display: none;">
                <button type="submit" value="Remove" class = "container1" style="width: 150px;">Remove</button>
         </form> 
  </td
  </tr>
    ''' % (str(index+1), groupTasks[index][0], groupTasks[index][1], groupTasks[index][0], groupTasks[index][1])

  display += '''</table>
  <h3> You want to assign the tasks for this week? Be careful and use the button below wisely! </h3>
  <input type="button" style = "background: #DF7F7F; padding: 12px 20px; margin: 8px 0; color: white;border: 1px solid #ccc; border-radius: 4px; box-sizing: border-box; font-size: 13px; " value="Assign tasks" onclick="window.location.href='/Rotator/cgi-bin/assigningTasks.cgi';">
  <h3> Do you want to add a new task? </h3>
                      <form action="addNewTask.cgi" method="post"> 
                        <h3> New task's name: </h3><input type="text" name="taskName" placeholder="Task name" class = "container1" style="background: white" id = "taskName">
                        <h3> New task's difficulty: </h3><input type="text" name="taskDiff" placeholder="(Average is 1000)" class = "container1" style="background: white" id = "taskDiff">
                        <button type="submit" value="Add" class = "container1" style="width: 150px;">Add</button>
                      </form> 
    <table>
      <tr>
        <th class = "weekDays">Name</th>
        <th class = "weekDays">Score</th>
        <th class = "weekDays">Remove</th>
      </tr>
              '''
  cursor.execute("SELECT User.Name, User_Group_Log.Work_Score, User.ID FROM User INNER JOIN User_Group_Log ON User.ID = User_Group_Log.User_ID WHERE User_Group_Log.Group_ID = %s" % (groupName[1]) )                
  users = cursor.fetchall()
  for user in users:
    display += '''
      <tr>
        <td class = "task">%s</td>
        <td class = "task">%s</td>
        <td class = "task">
                 <form action="removeUser.cgi" method="post"> 
                        <input type="text" name="userID" value=%s class = "container1" style="display: none;">
                        <button type="submit" value="Remove" class = "container1" style="width: 150px;">Remove</button>
                 </form> 
          </td
      </tr>
       ''' % (user[0], user[1], user[2])
  display +=  ''' </table>    
	</div> '''
display +=	'''		</div>

</body>
</div>''' 

cursor.close()
connection.close()

print display
