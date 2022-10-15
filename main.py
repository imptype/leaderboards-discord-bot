import os
from deta_discord_interactions import DiscordInteractions, Member

app = DiscordInteractions()
staff_role_id = 1030830480444108820#os.getenv('STAFF_ROLE_ID')

def get_role_ids(roles):
    return [role.id for role in roles]

@app.command(description = 'Ping the bot')
def ping(ctx):
    return 'Pong!'

@app.command(name = '1v1', description = 'Execute 1v1 match results')
def _1v1(ctx, winner : Member, loser : Member):
    if staff_role_id not in get_role_ids(ctx.author.roles):
        return 'You are not staff'
    return 'Pong!'

@app.command(description = 'Gets a user\'s points')
def getpoints(ctx, user : Member):
    return 'Pong!'

@app.command(description = 'Sets a user\'s points')
def setpoints(ctx, user : Member, points : int):
    if staff_role_id not in ctx.author.roles:
        return 'You are not staff'
    return 'Pong!'

@app.command(description = 'Gets everyone\'s points')
def getall(ctx, user : Member, points : int):
    return 'Pong!'

@app.route('/')
def index(request, start_response, abort):
    start_response('200 OK', [])
    return ['Home'.encode('UTF-8')]

@app.route('/update_commands')
def home(request, start_response, abort):
    app.update_commands(from_inside_a_micro=True)
    start_response('200 OK', [])
    return ['updated commands'.encode('UTF-8')]
