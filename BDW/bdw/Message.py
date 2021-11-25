from .comm import *
from .Channel import *
from .Guild import *
from .User import *
from .ext.components import *

class Message:
  id = 0
  channel = None 
  # guild = None
  author = 0
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
  def __init__(self, dataraw, bot):
    self.id = dataraw["id"]
    self.channel = Channel(APIcall(f"/channels/{dataraw['channel_id']}", "GET", bot.auth, {}), bot)
    self.author = dataraw["author"]["id"]
    self.author = User(APIcall(f"/users/{self.author}", "GET", bot.auth, None))
    self.msgtype = dataraw["type"]
    self.content = dataraw["content"]
    self.timestamp = dataraw["timestamp"]
    self.etimestamp = dataraw["edited_timestamp"]
    self.tts = dataraw["tts"]
    self.attachments = dataraw["attachments"]
    self.embeds = dataraw["embeds"]
    self.pinned = dataraw["pinned"]
    self.components = dataraw["components"]
    try:
      self.reaction = dataraw["reactions"]
    except:
      pass
    # if dataraw.__contains__("guild_id"):
    #   self.guild = Guild(dataraw["guild_id"], bot)