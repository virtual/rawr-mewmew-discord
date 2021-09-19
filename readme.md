# Discord bot

```
python3 -m pip install -U python-dotenv
python3 -m pip install -U apiclient
python3 -m pip install --upgrade google-api-python-client
python3 -m pip install -U discord.py[voice]
```

For Mac, if there are SSL errors, go to Applications > Python, Install Certs

## Dev

```
python3 bot.py
```

### .env file setup

Create `.env` file; this should never be committed to GitHub:

```
DISCORD_TOKEN=discordapptoken
YOUTUBE_KEY=youtubeapikey
```