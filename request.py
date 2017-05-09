import urllib.request
req = urllib.request.Request('http://www.upm.es')
response = urllib.request.urlopen(req)
the_page = response.read()