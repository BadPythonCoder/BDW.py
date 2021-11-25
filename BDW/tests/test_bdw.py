import bdw, os
from bdw.Intents import *
from bdw.ext import components, Interaction

auth = os.environ["auth"]

def test_bot_working():
  bot = bdw.Bot([INTENTS.GUILD_MESSAGES, INTENTS.GUILDS])
  @bot.event
  def ready(d):
    print("lets goo")
  @bot.event
  def interaction_create(d):
    # msg = bdw.Channel(bdw.APIcall("/channels/"+str(d['message']['channel_id']), "GET", bot.auth, {}), bot)
    interaction = Interaction.Interaction(d,bot)
    print("aight, something is duc")
    bdw.comm.APIcall(f"/interactions/{d['id']}/{d['token']}/callback", 'POST', bot.auth, {
      "type": 4,
      "data" : {
        "content": "W H A T ?"
      }
    })
  @bot.event
  def message_create(d):
    msg = bdw.Message(d, bot)
    if msg.content == "^test":
      embed = bdw.Embed("this is an embed test", "yaz", 0x00FFFF)
      embed.add_field("test","This is a field test")
      embed.add_field("test2","Inline test!",True)
      embed.set_footer("footer test")
      embed.set_author("coder() is actually a duck!")
      buton = components.Button("BUTTONTEST1","this is a test", 1)
      actionrow = components.ActionRow([buton])
      msg.channel.send("testduck", components=[actionrow])
  bot.start(auth)
  assert 5 == 6 # i still want all print statements to actually, well, print so that is why i do assertion error