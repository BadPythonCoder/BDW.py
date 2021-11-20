from .comm import *
from .Channel import *
from .Guild import *

class ContextBase:
  def __init__(self, dataraw):
    self.dataraw = dataraw
  def setdata(self, name, data):
    exec(f"self.{name} = {data}")

class Message(ContextBase):
  id = 0 #
  channel = None 
  guild = None
  author = 0 # EH
  content = ""
  timestamp = 0
  etimestamp = 0
  tts = False
  attachments = [] # EH
  embeds = [] # EH
  reactions = [] # EH
  pinned = False
  msgtype = 0
  components = [] # EH
  def process(self, bot):
    self.id = self.dataraw["id"]
    self.guild = Guild(self.dataraw["guild_id"], bot)
    self.channel = Channel(APIcall(f"/channels/{self.dataraw['channel_id']}", "GET", bot.auth, {}), bot)
    self.author = self.dataraw["author"]
    self.msgtype = self.dataraw["type"]
    self.content = self.dataraw["content"]
    self.timestamp = self.dataraw["timestamp"]
    self.etimestamp = self.dataraw["edited_timestamp"]
    self.tts = self.dataraw["tts"]
    self.attachments = self.dataraw["attachments"]
    self.embeds = self.dataraw["embeds"]
    self.reactions = self.dataraw["reactions"]
    self.pinned = self.dataraw["pinned"]
    self.components = self.dataraw["components"]