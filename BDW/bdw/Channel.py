from .comm import *
from .Embed import Embed

class Channel:
  def __init__(self, rawdata, bot):
    self.bot = bot
    self.raw = rawdata
    self.id = rawdata["id"]
    self.position = rawdata["position"]
    self.name = rawdata["name"]
    self.nsfw = rawdata["nsfw"]
    self.guild = rawdata["guild_id"]
    self.parent_id = rawdata["parent_id"]
    self.permission_overwries = rawdata["permission_overwrites"]
    if rawdata["type"] == 0:
      self.type = "text_channel"
      self.topic = rawdata["topic"]
      self.RLPU = rawdata["rate_limit_per_user"]
      self.banner = rawdata["banner"]
    elif rawdata["type"] == 2:
      self.type = "voice_channel"
      self.bitrate = rawdata["bitrate"]
      self.userlimit = rawdata["user_limit"]
      self.region = rawdata["rtc_region"]
    elif rawdata["type"] == 4:
      self.type = "category_channel"
    elif rawdata["type"] == 5:
      self.type = "announcement_channel"
    elif rawdata["type"] == 13:
      self.type = "stage_channel"
      self.bitrate = rawdata["bitrate"]
      self.userlimit = rawdata["user_limit"]
      self.region = rawdata["rtc_region"]
  def send(self, content=None, embeds=[], tts=False):
    if self.type == "text_channel" or self.type == "announcement_channel":
      embedsreal = []
      for embedobj in embeds:
        if isinstance(embedobj, Embed):
          embedsreal.append(embedobj.getObj())
        else:
          embedsreal.append(embedobj);
      APIcall(f"/channels/{self.id}/messages", "POST", self.bot.auth, {
        "content": content,
        "tts": tts,
        "embeds": embedsreal
      })
    else:
      raise APIerror("Cannot send in a non-text channel")