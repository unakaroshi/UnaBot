# UnaBot - Serverless

For fun and practise the Unabot is converted to a Serverless application.

This is built on Google Cloud Functions.
Cloud functions will automatically generate an HTTPS endpoint for you, so there's no need to work with an extra API Gateway.

## Add commands
In order to add commands you will need to do 2 steps: 
- register them with Discord
- deploy the cloud function code

### Registering commands
Check out the [scripts](/scripts/) directory. There you will find the script to register your function.  
Essentially this will post an HTTP call to the Discord API to make your command known.

### Deploying the code
```
    gcloud functions deploy <your function name> \
    --runtime python38 \
    --trigger-http \
    --allow-unauthenticated \
    --region=europe-west3 \
    --set-env-vars DISCORD_PUBLIC_KEY=<Discord BOT Public Key> \
```

The deployment will create an HTTPS endpoint for your function and print it into your console.

## Future ideas:
- CI/CD (Google Code Build or Github Actions)
- Unit Tests
- Serverless or Terraform Framework (infrastructure as code)