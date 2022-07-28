import random
import math

def respond(event):
  print(event)
  # init default difficulty == 1 => not change in roll result
  difficulty = 1
  # get options from command
  data = event['data']
  # check if options are set
  if "options" in data:
    options = data['options']
    for opt in options:
      if opt['name'] == 'threshold':
        print("Threshold value:")
        print(opt['value'])
        threshold = opt['value']
      if opt['name'] == 'difficulty':
        print("Difficulty value:")
        print(opt['value'])
        # adjust difficulty
        difficulty = opt['value']

  
  #roll the dice
  roll = random.randint(1,100)
  adjusted_threshold = math.ceil(int(threshold) / int(difficulty))
  
  if threshold != None:
    # divide roll result with difficulty rating and compare to threshold
    if roll <= adjusted_threshold:
      result = "**SUCCESS!**\n"
    else:
      result = "**FAIL!**\n"
    if difficulty != 1:
      result += "Reduced threshold from " + str(threshold) + " to " + str(adjusted_threshold)+ "\n"
    result += "You rolled: " + str(roll) + "\nYou needed: " + str(adjusted_threshold) 
  else:
    # no threshold given
    result = "You rolled: " + str(roll)

  # respond to command
  return {"type": 4, "data": {"content": result}}

def register():
  return {
   "name": "w100check",
   "type": 1,
   "description": "Roll W100 against a threshold, you can optionally select a difficulty (normal, hard, extreme)",
   "options": [{
        "name": "threshold",
        "description": "Which value do you need to beat?",
        "type": 4,
        "required": 1,
        "min_value": 2,
        "max_value": 99
      },
      {
        "name": "difficulty",
        "description": "Define your check difficulty",
        "type": 3,
        "required": 0,
        "choices": [
            {
                "name": "normal",
                "value": "1"
            },
            {
                "name": "hard",
                "value": "2"
            },
            {
                "name": "extreme",
                "value": "5"
            }
        ]
      }
   ]
}