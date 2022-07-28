import random

def respond(event):
  #roll the dice
  roll = random.randint(1,100)
  return {"type": 4, "data": {"content": "You rolled: " + str(roll)}}

def register():
  return {
   "name": "w100",
   "type": 1,
   "description": "Roll a single W100 dice.",
}