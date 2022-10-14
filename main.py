import os
from flask import Flask
from deta_discord_interactions import DiscordInteractions  

app = Flask(__name__)  # notice that the app instance is called `app`, this is very important.
discord = DiscordInteractions(app)

app.config["DISCORD_CLIENT_ID"] = os.environ["DISCORD_CLIENT_ID"]
app.config["DISCORD_PUBLIC_KEY"] = os.environ["DISCORD_PUBLIC_KEY"]
app.config["DISCORD_CLIENT_SECRET"] = os.environ["DISCORD_CLIENT_SECRET"]

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#@discord.command()
#def ping(ctx):
#    "Respond with a friendly 'pong'!"
#    return "Pong!"
