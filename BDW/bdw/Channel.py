from .comm import *
from .Embed import Embed
from .Guild import *
from .User import *
from .ext.slashcommands import *

class Message:
  '''
  This is used to get the message data, this is technically not implemented because the attachments, embeds, reactions and components are still just raw.
  '''
  id = 0
  channel = None 
  guild = None
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
    self.bot = bot
    self.id = dataraw["id"]
    self.author = dataraw["author"]["id"]
    self.author = User(APIcall(f"/users/{self.author}", "GET", bot.auth, None), bot)
    self.msgtype = dataraw["type"]
    self.content = dataraw["content"]
    self.timestamp = dataraw["timestamp"]
    self.etimestamp = dataraw["edited_timestamp"]
    self.tts = dataraw["tts"]
    self.attachments = dataraw["attachments"]
    self.embeds = dataraw["embeds"]
    self.pinned = dataraw["pinned"]
    self.components = dataraw["components"]
    if dataraw.__contains__("channel_id"):
      self.channel = Channel(APIcall(f"/channels/{dataraw['channel_id']}", "GET", bot.auth, {}), bot)
    try:
      self.reaction = dataraw["reactions"]
    except:
      pass
    # if dataraw.__contains__("guild_id"):
    #   self.guild = Guild(dataraw["guild_id"], bot)
  def edit(self, content=None, embeds=[], components= []):
    embedsreal = []
    componentsreal = []
    for embedobj in embeds:
      if isinstance(embedobj, Embed):
        embedsreal.append(embedobj.getObj())
      else:
        embedsreal.append(embedobj);
    for componentobj in components:
      componentsreal.append(componentobj.getOBJ())
    APIcall(f"/channels/{self.channel.id}/messages/{self.id}", "PATCH", self.bot.auth, {
      "content": content,
      "embeds": embedsreal,
      "components": componentsreal
    })
  def delete(self):
    APIcall(f"/channels/{self.channel.id}/messages/{self.id}", "DELETE", self.bot.auth, {})
    del self
  def reply(self, content="", embeds=[], components= [], tts=False):
    embedsreal = []
    componentsreal = []
    for embedobj in embeds:
      if isinstance(embedobj, Embed):
        embedsreal.append(embedobj.getObj())
      else:
        embedsreal.append(embedobj);
    for componentobj in components:
      componentsreal.append(componentobj.getOBJ())
    referenceDuc = {"message_id": self.id, "channel_id": self.channel.id}
    return Message(APIcall(f"/channels/{self.channel.id}/messages", "POST", self.bot.auth, {
      "content": content,
      "tts": tts,
      "embeds": embedsreal,
      "components": componentsreal,
      "message_reference": referenceDuc
    }),self.bot)

class Channel:
  '''
  This is the channel object which uses the rawdata from an event or somewhere else and uses the bot for authorization.
  '''
  def __init__(self, rawdata, bot):
    self.bot = bot
    self.raw = rawdata
    self.id = rawdata["id"]
    if rawdata["type"] == 0:
      self.type = "text_channel"
      self.topic = rawdata["topic"]
      self.RLPU = rawdata["rate_limit_per_user"]
      self.banner = rawdata["banner"]
      self.nsfw = rawdata["nsfw"]
      self.parent_id = rawdata["parent_id"]
      self.name = rawdata["name"]
      self.position = rawdata["position"]
    elif rawdata["type"] == 1:
      self.type = "DM_channel"
      self.recipients = rawdata["recipients"]
    elif rawdata["type"] == 2:
      self.type = "voice_channel"
      self.bitrate = rawdata["bitrate"]
      self.userlimit = rawdata["user_limit"]
      self.region = rawdata["rtc_region"]
      self.parent_id = rawdata["parent_id"]
      self.position = rawdata["position"]
      self.name = rawdata["name"]
      self.nsfw = rawdata["nsfw"]
    elif rawdata["type"] == 4:
      self.type = "category_channel"
      self.parent_id = rawdata["parent_id"]
      self.position = rawdata["position"]
      self.name = rawdata["name"]
    elif rawdata["type"] == 5:
      self.type = "announcement_channel"
      self.position = rawdata["position"]
      self.parent_id = rawdata["parent_id"]
      self.name = rawdata["name"]
      self.nsfw = rawdata["nsfw"]
    elif rawdata["type"] == 13:
      self.type = "stage_channel"
      self.bitrate = rawdata["bitrate"]
      self.userlimit = rawdata["user_limit"]
      self.region = rawdata["rtc_region"]
      self.parent_id = rawdata["parent_id"]
      self.name = rawdata["name"]
      self.nsfw = rawdata["nsfw"]
      self.position = rawdata["position"]
  def send(self, content=None, embeds=[], components= [], tts=False):
    if self.type == "text_channel" or self.type == "announcement_channel" or self.type == "DM_channel":
      embedsreal = []
      componentsreal = []
      for embedobj in embeds:
        if isinstance(embedobj, Embed):
          embedsreal.append(embedobj.getObj())
        else:
          embedsreal.append(embedobj);
      for componentobj in components:
        componentsreal.append(componentobj.getOBJ())
      return Message(APIcall(f"/channels/{self.id}/messages", "POST", self.bot.auth, {
        "content": content,
        "tts": tts,
        "embeds": embedsreal,
        "components": componentsreal
      }),self.bot)
    else:
      raise APIerror("Cannot send in a non-text channel")