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
    print ' <meta http-equiv="refresh" content="3;url=../login.html" />  '
#end of that section 
connection = mysql.connector.connect(
  user="mbyxadr2", database="2017_comp10120_z8", password="fA+h0m5_", host = "dbhost.cs.man.ac.uk"
  )

cursor = connection.cursor(buffered = True)

cursor.execute("SELECT Name, Email, Phone FROM User WHERE ID = %s" % userId)

details = cursor.fetchall()[0] #details[0] = name, details[1] = email, details[2] = phone

print '''
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
  	</style>

	<link href="https://fonts.googleapis.com/css?family=Open+Sans&amp;subset=cyrillic-ext" rel="stylesheet">   <meta charset="UTF-8">
	  <link rel="stylesheet" href="styles.css">

	<!-- Just tried to add a little title image, I know its not the logo -->
	<link rel="icon" type="image/gif/png" href="logo.png">

	<title>Settings</title>
</head>

<body>

		<div class="container">
			<h1><font color="#1d201f" size="20">Settings</font></h1>
			<div class="centered">
                <br>
                <button type="submit" value="Personal" onclick="document.getElementById('personalSettings').style.display='block'; document.getElementById('groupSettings').style.display='none'; " class = "container1">Personal</button>
                  <div id="personalSettings" style="display: none;">
                    <p>%s %s %s</p>
                  </div>
                <br>
                <button type="submit" value="Submit" onclick="document.getElementById('personalSettings').style.display='none'; document.getElementById('groupSettings').style.display='block'; " class = "container1">Group</button>
                  <div id="groupSettings" style="display: none;">
                    <p>Group Settings:</p>
                  </div>
			</div>
		</div>

</body>
</div>''' % (details)#HTML here


cursor.close()
connection.close()
