#!/usr/bin/env python
print "Content-Type: text/html"
print
print "<TITLE> Schedule </TITLE>"
import cgi
import requests

session = requests.Session()

session.get('http://10.2.232.136/Rotator/cgi-bin/timetable.cgi')
print session.cookies.get_dict()
