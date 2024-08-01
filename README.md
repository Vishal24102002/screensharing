# screenshare_lib

## Installation of Library
<pre><code> pip install screenshare </code></pre>

## From Server-Side
<pre lang='sh'>
from screenshare import server

host=socket.gethostname()
ser=server(host)
ser.create()
</pre>

## From Client-Side
<pre lang='sh'>
from pypi.screenshare import server_receive
  
ser=server_receive(host="Dell",port=8080)
ser.connect()
</pre>

