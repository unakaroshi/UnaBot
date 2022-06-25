
import random

def generateQuote():
    got_quotes = [
        (
            '**Never forget what you are. '
            'The rest of the world will not. '
            'Wear it like armor, and it can never '
            'be used to hurt you.**\r\n'
            '*Tyrion’s sage advice to Jon about being a bastard*'
        ),
        (
            '**There is only one thing we say to death: Not today.**\r\n'
            '*Swordsman extraordinaire Syrio Forel to Arya, while teaching her how to fight*'
        )
    ]
    
    return random.choice(got_quotes)    
    