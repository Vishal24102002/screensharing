# Screenshare_Lib
Screenshare: Python module for sharing/casting your screen with others in realtime
&amp; fast and accurate casting. Works best when connected to same network  Copyright © 2024 Coder-wis
<vishalsharma.pypi@gmail.com>

## Coming updates :
<ol>
  <li> Mouse Controlling </li>
  <li> Voice Transfer features </li>
</ol>

## Installation of Library :

The pip command to install ttkinter videos library for use
<pre><code> pip install screenshare </code></pre>

## Usage :

### From Server-Side :
<pre lang='sh'>
from screenshare import server
import socket

host=socket.gethostname()
print(host)
ser=server(host)
ser.create()
</pre>

### From Client-Side :
<pre lang='sh'>
from pypi.screenshare import server_receive
  
ser=server_receive(host="Dell",port=8080)
ser.connect()
</pre>

## Releases :
For the updated version <b><a href="">Latest</a></b> version.

## License :
Distributed under the MIT License. See <b><a href="https://github.com/Vishal24102002/screenshare_lib/blob/main/LICENSE"> LICENSE </a></b>for more information.
