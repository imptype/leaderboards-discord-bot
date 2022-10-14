import os
import sys

from flask import Flask

#from deta_discord_interactions import DiscordInteractions  # noqa: E402


app = Flask(__name__)
#discord = DiscordInteractions(app)

# Find these in your Discord Developer Portal, store them as environment vars
app.config["DISCORD_CLIENT_ID"] = os.environ["DISCORD_CLIENT_ID"]
app.config["DISCORD_PUBLIC_KEY"] = os.environ["DISCORD_PUBLIC_KEY"]
app.config["DISCORD_CLIENT_SECRET"] = os.environ["DISCORD_CLIENT_SECRET"]


# Clear any existing global application commands
# discord.update_commands()


# Simplest type of command: respond with a string
#@discord.command()
#def ping(ctx):
#    "Respond with a friendly 'pong'!"
#    return "Pong!"


@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'

@app.route('/hello2')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World2'


# This is the URL that your app will listen for Discord Interactions on
# Put this into the developer portal
#discord.set_route("/interactions")


# Register application commands with this
# (omit guild_id parameter to register global commands,
# but note that these can take up to 1 hour to be registered)
# This also removes old/unused commands
# discord.update_commands(guild_id=os.environ["TESTING_GUILD"])


if __name__ == "__main__":
    app.run()
