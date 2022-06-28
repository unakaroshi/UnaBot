import random
import re

random.seed()

def parseRollCommand(cmd):
    cmd = cmd.upper()
    cmd = cmd.replace("D", "W")
    
    if re.search(r"^[-+]?[0-9]+W[-+]?[0-9]+$", cmd) == None:
        return (0,0)
    
    
    parts = cmd.split("W")        
    if len(parts) < 2 or len(parts) > 2: 
        return (0,0)
    
    dice_number = int(parts[0])
    dice_sides = int(parts[1])
    
    return (dice_number, dice_sides)



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



def handleDiceRequest(dice_number, dice_sides):   
    response = ""
    #response = "Rolling {} dices...\n\n".format(dice_number)
    dicerolls = rollDices(dice_number, dice_sides)
    
    response += ", ".join(str(elem) for elem in dicerolls)
          
    response += "\n--------------\n"
    response += "**Total: {:5d}**".format(sum(dicerolls))
    
    return response
    
    
if __name__ == "__main__":
     print ("No tests here yet")
    
     