import functions_framework
#from discord.ext import commands
import json
import os
#from helpers import request_verification
from google.cloud import logging
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from flask import abort


# Decouple Cloud Function event handler from bot-specific code
# Discord endpoint requirements: https://discord.com/developers/docs/interactions/receiving-and-responding#receiving-an-interaction

@functions_framework.http
def unabot(request):

  # Instantiates a client
  logging_client = logging.Client()

  # The name of the log to write to
  log_name = "UnaBot-log"
  # Selects the log to write to
  logger = logging_client.logger(log_name)
  
  # log request for debugging
  logger.log_struct(dict(request.headers))
  logger.log_struct(request.json)
  
  # Your public key can be found on your application in the Developer Portal
  PUBLIC_KEY = os.environ.get('DISCORD_PUBLIC_KEY', None)
  if PUBLIC_KEY is None:
    print("No Public Key deployed! Check your cloud function variables!")
    abort(401, 'invalid request signature')

  verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))

  signature = request.headers["X-Signature-Ed25519"]
  timestamp = request.headers["X-Signature-Timestamp"]
  rawbody = request.get_data().decode("utf-8")
  # print("Raw body")
  # print(body)

  # print("Signature")
  # print(signature)

  # print("Timestamp")
  # print(timestamp)


  try:
      verify_key.verify(f'{timestamp}{rawbody}'.encode(), bytes.fromhex(signature))
  except BadSignatureError as e:
      logger.log_text("Signature Check failed!", severity="ERROR")
      print(e)
      abort(401, 'invalid request signature')

  # get request data as JSON
  payload = request.json
 
  # add option to reply to ping (Discord endpoints requirement 2)
  if payload['type'] == 1:
    return {"type": 1}
  
  # add other slash commands
  if payload['data']['name'] == 'foo':
    # do help action
    return {"type": 4, "data": {"content": "No rest for the wicked!"}}
    