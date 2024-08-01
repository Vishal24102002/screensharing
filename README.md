# Screenshare_Lib

## Installation of Library
<pre><code> pip install screenshare </code></pre>

## From Server-Side
<pre lang='sh'>
from screenshare import server
import socket

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

<h3>License</h3>
Distributed under the MIT License. See <b><a href="https://github.com/Vishal24102002/screenshare_lib/blob/main/LICENSE"> LICENSE </a></b>for more information.
