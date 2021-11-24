import bdw, os
from bdw.Intents import *

auth = os.environ["auth"]

def test_bot_working():
  bot = bdw.Bot([INTENTS.GUILD_MESSAGES, INTENTS.GUILDS])
  @bot.event
  def ready(d):
    print("lets goo")
  @bot.event
  def message_create(d):
    msg = bdw.Message(d, bot)
    if msg.content == "^test":
      msg.channel.send("no ducking way")
  bot.start(auth)
  assert 5 == 6 # i still want all print statements to actually, well, print so that is why i do assertion error