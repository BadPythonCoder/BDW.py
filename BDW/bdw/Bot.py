from .comm import *
from .Intents import *
import websocket, threading, json, time

class Bot:
  def __init__(self, intents=[]):
    self.guilds = []
    self.intents = IG(intents)
    self.s = None
  def start(self, auth):
    self.guilds = APIcall("/users/@me/guilds","GET", auth,{})
    # Begin Gateway
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
  def on_message(self, ws, msg):
      data = json.loads(msg)
      self.s = data["s"]
      if data["op"] == 10:
        authorization = {
          "op": 2,
          "t": None,
          "s": None,
          "d": {
            "token": auth,
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
    # End Gateway 