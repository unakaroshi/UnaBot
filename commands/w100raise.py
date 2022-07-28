import random

def respond(event):
  print(event)
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

  # roll the dice
  roll = random.randint(1,100)
    
  if threshold != None:
    # divide roll result with difficulty rating and compare to threshold
    if roll >= threshold:
      result = "**SUCCESS!**\n"
      result += "You earned **" + str(random.randint(1,10)) + "** points!"
    else:
      result = "**FAIL!**\n"    
  else:
    # no threshold given
    result = "You better tell me your current attribute / skill value if you want to raise something!"

  # respond to command
  return {"type": 4, "data": {"content": result}}

def register():
  return {
   "name": "w100raise",
   "type": 1,
   "description": "Try to raise a W100 attribute.",
   "options": [{
        "name": "threshold",
        "description": "Enter your current attribute or skill value which you want to raise.",
        "type": 4,
        "required": 1,
        "min_value": 1,
        "max_value": 100
      }      
   ]
}