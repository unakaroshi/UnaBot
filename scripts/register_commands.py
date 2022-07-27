#!/usr/bin/env python
"""Discord Command Registration Script

This script registers your available bot commands in Discord.
When you add or update a command, you will need to run this script before the command becomes available in Discord.

In order to register commands you will need to use some sensitive data (i.e. Discord Bot Token).
To make things safer, these are stored in the GCLOUD Secrets Manager and read during runtime from there.
If you experince any troubles, please check your IAM permissions!

This script is NOT uploaded to Google Cloud, instead it needs to be run locally (or in future during CI/CD) before deploying your bot code to the cloud.
"""

import requests
import os, sys
from google.cloud import secretmanager
from importlib import import_module

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

# init GCLOUD Secrets Manager
secrets = secretmanager.SecretManagerServiceClient()
BOT_TOKEN = secrets.access_secret_version(request={"name": "projects/571203715515/secrets/CatLoverBotToken/versions/1"}).payload.data.decode("utf-8")
APP_ID = secrets.access_secret_version(request={"name": "projects/571203715515/secrets/CatLoverDiscordBotAppID/versions/1"}).payload.data.decode("utf-8")

url = "https://discord.com/api/v10/applications/" + APP_ID + "/commands"

headers = {
   "Authorization": "Bot " + BOT_TOKEN,
   "Content-Type": "application/json"
}

# command_data = {
#    "name": "foo",
#    "type": 1,
#    "description": "replies with bar ;/",
# }
    
path_of_the_directory= '../commands'

for filename in os.listdir(path_of_the_directory):
    f = os.path.join(path_of_the_directory,filename)
    if os.path.isfile(f) and filename != "__init__.py":
      commandModule = import_module("commands."+filename.split(".")[0])
      comResponse = getattr(commandModule, "register")

      command_data = comResponse()
      #print(command_data)
      x = requests.post(url, json = command_data, headers = headers)
      print(x.text)

