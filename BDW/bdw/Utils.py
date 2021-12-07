from .Channel import *
from .comm import *
from .Message import *

def get_message_with_id(channelid, messageid, bot) -> Message:
  return Message(APIcall(f"/channels/{channelid}/messages/{messageid}", "GET", bot.auth, {}),bot)
