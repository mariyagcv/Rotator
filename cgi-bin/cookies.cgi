#!/usr/bin/env python
print "Content-Type: text/html"
print
print "<TITLE> Cookies! </TITLE>"
print "<h1> Hey </h1>"

import os

handler = {}
if 'HTTP_COOKIE' in os.environ:
    cookies = os.environ['HTTP_COOKIE']
    cookies = cookies.split('; ')
    print cookies

    for cookie in cookies:
        cookie = cookie.split('=')
        handler[cookie[0]] = cookie[1]
        

print handler
for k in handler:
    print k + " = " + handler[k] + "<br>"
