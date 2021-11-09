# Look at the source code
# Realize that you have to send a HEAD request - which requests headers of the file - to the website
# Write script and run

import requests

output = requests.head("http://mercury.picoctf.net:15931/index.php")
print(output.headers)
