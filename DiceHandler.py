import random
import re

random.seed()

def rollDices(count, sides):
    """
    Rolls a variable number of dices with given sides   

    Args:
        count (int): Number of dices to roll
        sides (_type_): Number of sides the dices should have

    Returns:
        list: Sorted list of all rolled dices
    """
    result = list()
    for i in range(0,count):
        result.append(random.randrange(1,sides))
    result.sort()
    return result

def handleDiceRequest(param):
    """
    Gets a string like "!rd 5w6"

    Args:
        param (string): String must start with "!rd ", the following string
                        must exist of a number, the letter "w" or "W" and 
                        another number.
                        The first number is the number of dices to roll, 
                        the second number tells, how many sides the dice
                        has

    Returns:
        String: String to use for the discord bot
    """
    
    param = param.upper()
    
    if re.search(r"^[-+]?[0-9]+W[-+]?[0-9]+$", param) == None:
        return "Something like '!rd 5w6' would be okay"
    
    
    parts = param.split("W")        
    if len(parts) < 2 or len(parts) > 2: 
        return "I don't understand"
    
    dice_number = int(parts[0])
    dice_sides = int(parts[1])
        
    
    if (dice_number < 1) or (dice_number > 100):
      return "Yeah, try to bug me. (Only Dicenumbers between 1 and 100, please)"
      
  
    if (dice_sides < 3):
      return "How the f... can you build a {} sided dice? Try better next time.".format(dice_sides)
      
    
    if (dice_sides > 100):
      return "How many sides does your dice have? Are you Alex?"
     
    if dice_number == 1:
      return "Your result is: {}".format(random.randrange(1,dice_sides))
    
    
    response = "Rolling {} dices...\n\n".format(dice_number)
    dicerolls = rollDices(dice_number, dice_sides)
    
    response += ", ".join(str(elem) for elem in dicerolls)
          
    response += "\n--------------\n"
    response += "Total: {:5d}".format(sum(dicerolls))
    
    return response
    
    
if __name__ == "__main__":
    print ("Mainfile")
    
    commands = [
        "!rd 5w6",
        "!rd 5W6",
        "!rd  5W6 ",
        "!rd 5W6 ",
        "!rd 5W6",
        "!rd 5 W6",
        "!rd 5W 6",
        "!rd 5 W 6 ",
        "!rd 5d6",
        "!rd 100w100",
        "!rd -1w6",
        "!rd 5w1000",
        ]
    
    for cmd in commands: 
        print("\n\n================\n")
        print("   Command: '{}'\n\n".format(cmd))
              
        print (handleDiceRequest(cmd))        
        print("================\n")
     