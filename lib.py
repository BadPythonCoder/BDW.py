import requests
class DuckError(Exception):
  pass
class Bot:
  APIURL = "https://discord.com/api/v9"
  def __init__(self, auth):
    self.AUTH = auth
  def send(self, channel, message):
    r = requests.post(
      self.APIURL+f"/channels/{channel}/messages",
      headers={
        "Authorization": "Bot "+self.AUTH
      },
      data = {
        "content": message,
        "tts": False
      }
    )
    response = r.json()
    if response.__contains__("code"):
      raise DuckError(response["message"])