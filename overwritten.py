import requests
import json

BASE_URL = "https://api.github.com/repos/fawaz-strawberry/fawaz-strawberry.github.io/contents/"
# HEADERS = {"APCA-API-KEY-ID":API_KEY, "APCA-API-SECRET-KEY":SECRET_KEY}
HEADERS = {"Accept": "application/vnd.github.v3+json"}

import base64
data = open("C:/Users/Fawaz Mujtaba/Documents/GitHub/fawaz-strawberry.github.io/stock_data.js", "rb").read()
encoded = base64.b64encode(data)
#print(str(encoded))
#encoded = json.dumps(data)
DATA = {"message":"Updated Tickers", "content":encoded}

r = requests.get(url=BASE_URL, headers=HEADERS, auth=("fawaz-strawberry", "111afeb2b5ae9e423da762a4231fed92f03c7399"))
print(r.request.url)
print(json.loads(r.content))