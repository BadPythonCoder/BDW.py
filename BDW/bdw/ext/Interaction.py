from bdw.Message import *
from bdw.comm import *
from bdw.Channel import *
from bdw.User import *
from bdw.Guild import *
class InteractionType:
  PING = 1
  APPLICATION_COMMAND = 2
  MESSAGE_COMPONENT = 3
  APPLICATION_COMMAND_AUTOCOMPLETE = 4
class Interaction:
  def __init__(self, data, bot):
    self.raw = data
    self.token = data["token"]
    self.id = data["id"]
    self.bot = bot
    self.type = data["type"]
    self.appid = data["application_id"]
    if data.__contains__("message"):
      self.message = data["message"]['id']
      self.message = Message(APIcall(f"/channels/{data['channel_id']}/messages/{self.message}", "GET", bot.auth, {}), bot)
    if data.__contains__("guild_id"):
      self.guild = data["guild_id"]
      self.guild = Guild(self.guild, bot)
    if data.__contains__("user"):
      self.user = User(data["user"])
    if data.__contains__("channel_id"):
      self.channel = data["channel_id"]
      self.channel = Channel(APIcall(f"/channels/{self.channel}", "GET", bot.auth, {}), bot)
    if data.__contains__("data"):
      self.data = data["data"]
      print(self.data)
  def respond(self, content):
    APIcall(f"/interactions/{self.id}/{self.token}/callback", 'POST', self.bot.auth, {
      "type": 4,
      "data" : {
        "content": content
      }
    })