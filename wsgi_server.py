from wsgiref.simple_server import make_server
from WSGI import Application

httpd = make_server('',8000,Application)
print('Server HTTP on port 8000')
httpd.serve_forever()
