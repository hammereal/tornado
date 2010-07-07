from tornado import async_httplib2
h = async_httplib2.Http()
resp, content = h.request("http://www.google.com/", "GET")
print content
resp, content = h.request("http://www.baidu.com/");
print content