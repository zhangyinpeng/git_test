#import urllib2
from gzip import GzipFile
#from StringIO import StringIO
from io import StringIO
import zlib
 
def loadData(url):
    request = urllib2.Request(url)
    request.add_header('Accept-encoding', 'gzip,deflate')
    response = urllib2.urlopen(request)
    content = response.read()
    encoding = response.info().get('Content-Encoding')
    if encoding == 'gzip':
        content = gzip(content)
    elif encoding == 'deflate':
        content = deflate(content)
    return content
 
def gzip_(data):
    buf = StringIO(data)
    f = gzip.GzipFile(fileobj=buf)
    return f.read()
    
def myzlib(data):
    f = zlib.compress(data)
    #f = zlib.compress(data, zlib.DEFLATED)

    fileObject = open('myzlib', 'wb')  
    fileObject.write(f)  
    fileObject.close()  

    return f  
 
def deflate(data):
    try:
        return zlib.decompress(data, -zlib.MAX_WBITS)
    except zlib.error:
        return zlib.decompress(data)
 
'''
def main():
    url = "http://www.xxx.com/"
    content = loadData(url)
    print content
'''

import zlib

MESSAGE = b"life of brian"

compressed_message = zlib.compress(MESSAGE)
decompressed_message = zlib.decompress(compressed_message)

print ("original:", repr(MESSAGE))
print ("compressed message:", repr(compressed_message))
print ("decompressed message:", repr(decompressed_message))

print ("x"*20)
s_in = b'blob %d\0what is up, doc?'%(16)
print (s_in)
s_out = zlib.compress(s_in)
print (s_out)
print ("y"*20)
s_in = "blob 16\0what is up, doc?"
s_out = zlib.compress(s_in.encode())
print (s_out)
s_in = 'blob '+str(16)+'\0what is up, doc?'
s_in = 'blob {}\0what is up, doc?'.format(16)
s_out = zlib.compress(s_in.encode())
print (s_out)
print (s_out)
fff=open('yasuo', 'wb')
fff.write(s_out)
fff.close()
print ("yasuo file write end")
with open('yasuo2', 'rb') as fff:
    file_content = fff.read()
    print ("a"*20)
    print (file_content)
    print (deflate(file_content))
    print ("b"*20)
def main():
    content = b"what is up, doc?"
    header = 'blob '+str(len(content))+'\0'
    header = b'blob %d\0'%(len(content))
    store = header+content
    store = b"blob 16\0what is up, doc?"
    #print (gzip(store.encode()))
    print (myzlib(store))
    print (deflate(myzlib(store)))
    
 
if __name__ == '__main__':
    main()
