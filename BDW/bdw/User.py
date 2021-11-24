from .comm import *

class User:
  def __init__(self, raw):
    self.raw = raw
    self.id = raw["id"]
    self.username = raw["username"]
    self.discriminator = raw["discriminator"]
    self.pubflags = raw["public_flags"]
    self.banner = raw["banner"]
    self.avatarhash = raw["avatar"]
    self.bannercol = raw["banner_color"]
    self.accent = raw["accent_color"]
  def __repr__(self):
    return f"{self.username}#{self.discriminator}"