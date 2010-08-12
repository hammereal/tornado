from tornado import ioloop, httpclient

def handle_request(response):
    print response.body
    ioloop.IOLoop.instance().stop()
    
http_client = httpclient.AsyncHTTPClient()
http_client.fetch("http://www.python.org/", handle_request)
ioloop.IOLoop.instance().start()