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
      embed = bdw.Embed("this is an embed test", "yaz", 0x00FFFF)
      embed.add_field("test","This is a field test")
      embed.add_field("test2","Inline test!",True)
      embed.set_footer("footer test")
      embed.set_author("coder() is actually a duck!")
      msg.channel.send("testduck", embeds=[embed])
  bot.start(auth)
  assert 5 == 6 # i still want all print statements to actually, well, print so that is why i do assertion error