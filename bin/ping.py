#!/usr/bin/python
import socket
from urllib2 import urlopen, URLError, HTTPError
from os import environ

socket.setdefaulttimeout(23)

if environ.has_key('PING_URL'):
    url = environ.get('PING_URL')
    try:
        response = urlopen( url )
    except HTTPError, e:
        print 'The server could not fulfill the request. Reason: ', str(e.code)
    except URLError, e:
        print 'We failed to reach a server. Reason:', str(e.response)
    else:
        html = response.read()
        print 'got response!'
else:
    print 'no environment key PING_URL'
