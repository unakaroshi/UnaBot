import random
import re

random.seed()

def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))


def parseRollCommand(cmd):
    '''
    
    '''
    if cmd == None:
        return(1,6)
    
    cmd = cmd.upper()
    cmd = cmd.replace("D", "W")
    
    if re.search(r"^[-+]?[0-9]+W[-+]?[0-9]+$", cmd) == None:
        return (1,6)
    
    
    parts = cmd.split("W")        
    if len(parts) < 2 or len(parts) > 2: 
        return (1,6)
    
    dice_number = clamp(int(parts[0]),1,100)
    dice_sides = clamp(int(parts[1]),1,100)
    
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
        result.append(random.randrange(1,sides+1))
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
     
     print (int(99/2))
     print (int(99/5))
    
     