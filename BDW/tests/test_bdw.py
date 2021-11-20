import bdw, os
from bdw.Intents import *

auth = os.environ["auth"]

def test_bot_working():
  bot = bdw.Bot([INTENTS.GUILD_MESSAGES, INTENTS.GUILDS])
  @bot.event
  def ready():
    print("lets goo")
  bot.start(auth)
  assert 5 == 6 # i still want all print statements to actually, well, print so that is why i do assertion error