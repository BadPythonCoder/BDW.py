import bdw, os

auth = os.environ["auth"]

def test_bot_working():
  # bot = bdw.Bot(auth, [])
  # bot.start()
  print(bdw.comm.APIcall)
  # g = bdw.Guild(bot.guilds[0]["id"],auth)
  # g.channels[2].send("duck???")
  assert 5 == 6 # i still want all print statements to actually, well, print so that is why i do assertion error