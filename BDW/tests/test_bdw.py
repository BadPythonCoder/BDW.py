# import bdw, os, time
# from bdw.Intents import *
# from bdw.ext.slashcommands import *

# auth = os.environ["auth"]

# def test_bot_working():
#   bot = bdw.Bot([INTENTS.GUILD_MESSAGES, INTENTS.GUILDS])
#   testcmd = Slashcommand("test", "This is a test!", bot)
#   @bot.event
#   def ready(d):
#     # testcmd.register()
#     registerCommands([testcmd], bot)
#     print("lets goo")
#   @bot.event
#   def interaction_create(d):
#     print("interaction received")
#     interaction = Interaction(d,bot)
#     if interaction.type == InteractionType.MESSAGE_COMPONENT:
#       # interaction.respond(str(interaction.user)+", you are a sussy baka!")
#       interaction.respond("somebody clicked!!!11!1!")
#     elif interaction.type == InteractionType.APPLICATION_COMMAND:
#       interaction.respond("POGGERS, SLASH COMMAND WORKS!!!!")
#   @bot.event
#   def message_create(d):
#     msg = bdw.Message(d, bot)
#     if msg.content == "^test":
#       embed = bdw.Embed("this is an embed test", "yaz", 0x00FFFF)
#       embed.add_field("test","This is a field test")
#       embed.add_field("test2","Inline test!",True)
#       embed.set_footer("footer test")
#       embed.set_author("coder() is actually a duck!")
#       buton = Button("BUTTONTEST1","this is a test", 1)
#       actionrow = ActionRow([buton])
#       msg.channel.send("testduck", components=[actionrow])
#     if msg.content == "^reactions":
#       msg.react("😳")
#       msg.react("e_", True)
#   bot.start(auth)
#   assert 5 == 6 # i still want all print statements to actually, well, print so that is why i do assertion error