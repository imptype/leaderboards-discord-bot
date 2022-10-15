import os
from deta_discord_interactions import DiscordInteractions  

app = DiscordInteractions()

@app.command()
def ping(ctx):
    return 'Pong!'

@app.route('/')
def index(request, start_response, abort):
    start_response('200 OK', [])
    return ['Home'.encode('UTF-8')]

@app.route('/update_commands')
def home(request, start_response, abort):
    text = 'updated commands'
    try:
        app.update_commands(from_inside_a_micro=True)
    except Exception as e:
        text = str(e)
    start_response('200 OK', [])
    return [text.encode('UTF-8')]
