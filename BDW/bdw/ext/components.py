class ActionRow:
  componentOBJ = {}
  def __init__(self, components):
    self.componentOBJ["components"] = []
    for component in components:
      self.componentOBJ["components"].append(component.getOBJ())
    self.componentOBJ["type"] = 1
  def getOBJ(self):
    return self.componentOBJ

class Button:
  componentOBJ = {}
  def __init__(self, id, name, buttontype, enabled=True):
    self.componentOBJ["custom_id"] = id
    self.componentOBJ["label"] = name
    self.componentOBJ["type"] = 2
    self.componentOBJ["style"] = buttontype
    self.componentOBJ["disabled"] = not enabled
  def disable(self):
    self.componentOBJ["disabled"] = True
  def enable(self):
    self.componentOBJ["enable"] = True
  def getOBJ(self):
    return self.componentOBJ