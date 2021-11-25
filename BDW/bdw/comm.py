import requests

# Best error handling of **all time**
class APIerror(Exception):
  pass
def APIcall(URI, type, auth, payload):
  res = {}
  if type == "GET":
    res = requests.get("https://discord.com/api/v9"+URI, headers={"Authorization": "Bot "+auth}, data=payload).json()
  elif type == "POST":
    
    res = requests.post("https://discord.com/api/v9"+URI, headers={"Authorization": "Bot "+auth,"Content-Type": "application/json"}, json=payload).json()
  if res.__contains__("code"):
    raise APIerror(res)
  return res