#!/usr/bin/env python

import Cookie
import cgi

c = Cookie.SimpleCookie()
c['Rotator'] = ''
c['Rotator']['expires'] = 'Thu, 01 Jan 1970 00:00:00 GMT'

print c
print "Content-Type: text/html\n\n"
print
print '''
<html>
<TITLE> Logout Page </TITLE>
<body>
<link href="https://fonts.googleapis.com/css?family=Open+Sans&amp;subset=cyrillic-ext" rel="stylesheet">   <meta charset="UTF-8">
<link rel="stylesheet" href="../styles.css"> 
<h1> You have been logged out. </h1>
<meta http-equiv="refresh" content="0;url=../login.html" /> 
</body></html>
'''
