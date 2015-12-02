from urllib2 import Request, urlopen, URLError, HTTPError
req = Request('http://www.xyx.org')
try:
    response = urlopen(req)
except HTTPError as e:
    print 'The server couldn\'t fulfill the request.'
    print 'Error code: ', e.code
except URLError as e:
    print 'We failed to reach a server.'
    print 'Reason: ', e.reason
else:
    # everything is fine
    print "Nothing"
