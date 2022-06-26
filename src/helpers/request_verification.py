from nacl.signing import VerifyKey 
from nacl.exceptions import BadSignatureError
import json
import os

def verifySignatue (sig, timestamp, payload):
  # get public key from env
  pubKey = os.environ.get('DISCORD_PUBLIC_KEY', None)
  if pubKey is None:
    #TODO: log error
    return False
  
  # Sig check using pynacl
  verify_key = VerifyKey(bytes.fromhex(pubKey))
  
  try: 
      verify_key.verify(f'{timestamp}{body}'.encode(), bytes.fromhex(sig))
      body = json.loads(payload)
      if body["type"] == 1:
          return True
  except (BadSignatureError) as e:
      print('Signature Check failed!')
      return False