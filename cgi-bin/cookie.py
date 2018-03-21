from urllib2 import Request, build_opener, HTTPCookieProcessor, HTTPHandler
import cookielib


def status(url):
  jar = cookielib.CookieJar()
  opener = build_opener(HTTPCookieProcessor(jar), HTTPHandler())
  opener.open(Request(url) )
  for cookie in jar:
    if cookie.path== '/Rotator/cgi-bin':
      return True
  return False
  
def delete(url):
  jar = cookielib.CookieJar()
  opener = build_opener(HTTPCookieProcessor(jar), HTTPHandler())
  opener.open(Request(url))
  for cookie in jar:
    if cookie.path == '/Rotator/cgi-bin':
      jar.clear('10.2.232.136')

def showCookies():
	jar = 0
