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
from google.cloud import secretmanager

# init GCLOUD Secrets Manager
secrets = secretmanager.SecretManagerServiceClient()
BOT_TOKEN = secrets.access_secret_version(request={"name": "projects/571203715515/secrets/CatLoverBotToken/versions/1"}).payload.data.decode("utf-8")
APP_ID = secrets.access_secret_version(request={"name": "projects/571203715515/secrets/CatLoverDiscordBotAppID/versions/1"}).payload.data.decode("utf-8")
GUILD_ID = secrets.access_secret_version(request={"name": "projects/571203715515/secrets/BotdevdebugServerID/versions/1"}).payload.data.decode("utf-8")

url = "https://discord.com/api/v8/applications/" + APP_ID + "/guilds/" + GUILD_ID + "/commands"
print(url)
headers = {
   "Authorization": "Bot " + BOT_TOKEN,
   "Content-Type": "application/json"
}

print(headers)

command_data = {
   "name": "foo",
   "type": 1,
   "description": "replies with bar ;/",
}

x = requests.post(url, json = command_data, headers = headers)
print(x.text)

