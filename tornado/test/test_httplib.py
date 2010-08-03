from tornado import httplib


conn = httplib.HTTPConnection("www.ucla.edu")
conn.request("GET", "/")
r1 = conn.getresponse()
print r1.length, r1.status, r1.reason

data1 = r1.read()
print data1