from .comm import *
from .Intents import *
import websocket, threading, json, time

class Bot:
  def __init__(self, intents=[]):
    self.guilds = []
    self.intents = IG(intents)
    self.s = None
    self.bot = self
    self.events = {}
  def heartbeat(self, ws, interval):
    while True:
      time.sleep(interval*0.001)
      heartbeatdata = {
        "op": 1,
        "t": None,
        "s": None,
        "d": self.s
      }
      ws.send(json.dumps(heartbeatdata))
  # Events 
  def NTEV(self, EVN):
    return EVN.upper()
  def event(self, func):
    def eventwrapper():
      self.events[self.NTEV(func.__name__)] = func
    return eventwrapper()
  # Gate way stuff begin
  def on_message(self, ws, msg):
    data = json.loads(msg)
    self.s = data["s"]
    if data["op"] == 10:
      authorization = {
        "op": 2,
        "t": None,
        "s": None,
        "d": {
          "token": self.auth,
          "intents": self.intents.getIntent(),
          "properties": {
            "$os": "UDNSystems",
            "$browser": "Icefox",
            "$device": "Internet"
          }
        }
      }
      ws.send(json.dumps(authorization))
      self.heartbeatthread = threading.Thread(target=self.heartbeat, args=(ws, data["d"]["heartbeat_interval"],), daemon=True)
      self.heartbeatthread.start() 
    if data["op"] == 0:
      if self.events.__contains__(data["t"]):
        self.events[data["t"]](data["d"])
  def on_close(self, ws, status, msg):
    print("Closed connection with status code"+str(status)+". Last message: \n"+msg)
  def on_error(self, ws, err):
    print("ERROR DETECTED\n"+str(err))
  def on_ready(self, ws):
    pass
  # Gateway stuff end
  def start(self, auth):
    self.guilds = APIcall("/users/@me/guilds","GET", auth,{})
    self.botws = websocket.WebSocketApp(
      "wss://gateway.discord.gg/?v=9&encoding=json",
      on_open=self.on_ready,
      on_error=self.on_error,
      on_message=self.on_message,
      on_close=self.on_close
    )
    self.auth = auth
    self.wst = threading.Thread(target=self.botws.run_forever)
    self.wst.start()
