import random

def respond(event):
  print("w100 Command reached!")
  return {"type": 4, "data": {"content": "You rolled: " + str(random.randint(1,101))}}

def register():
  return {
   "name": "w100",
   "type": 1,
   "description": "Roll a single W100 dice.",
}