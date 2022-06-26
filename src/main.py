from discord.ext import commands
import json
from helpers import request_verification
import DiceHandler
import UnaBot

# Decouple Cloud Function event handler from bot-specific code

def unabot(request):
  
  # log request for debugging
  print(request)

  signature = request['headers']["x-signature-ed25519"] 
  timestamp = request['headers']["x-signature-timestamp"] 
  body = request['body']

  # verify request
  if request_verification.verifySignatue(signature, timestamp, body) is True:
    return {
              'statusCode': 200, 
              'body': json.dumps({'type': 1})
          } 
  else:
    return {
            'statusCode': 401, 
            'body': json.dumps("Bad Signature")
        }

  # TODO: add option to reply to ping

  # TODO: add other slash commands
  

  