

import requests

response=requests.get("https://zenquotes.io/api/random", timeout=10)

response.raise_for_status()

data=response.json()


print(data[0]["q"])