import os
from deta import Base
from deta_discord_interactions import DiscordInteractions, Member, Embed

db = Base('ranks')
app = DiscordInteractions()
staff_role_id = os.getenv('STAFF_ROLE_ID')

def get_points(user_id):
  row = db.get(str(user_id))
  if row:
    return row['points']
  return 0

def update_points(user_id, points):
  db.put({'points' : points}, key = str(user_id))

@app.command(description = 'Ping the bot')
def ping(ctx):
    return 'Pong!'

@app.command(name = '1v1', description = 'Execute 1v1 match results')
def _1v1(ctx, winner : Member, loser : Member):
    
    if staff_role_id not in ctx.author.roles:
        return 'You are not staff.'
    
    old_winner_points = get_points(winner.id)
    new_winner_points = old_winner_points + 5
    update_points(winner.id, new_winner_points)
    
    old_loser_points = get_points(loser.id)
    new_loser_points = old_loser_points - 5
    update_points(loser.id, new_loser_points)
    
    text = '\n'.join([
        '1v1 Match Results:',
        'Winner: {} (`{}` -> `{}`)'.format(winner.mention, old_winner_points, new_winner_points),
        'Loser: {} (`{}` -> `{}`)'.format(loser.mention, old_loser_points, new_loser_points)
    ])
    
    return text

@app.command(description = 'Gets a user\'s points')
def getpoints(ctx, user : Member):
    points = get_points(user.id)
    text = '{}\'s points: `{}`'.format(user.username, points)
    return text

@app.command(description = 'Sets a user\'s points')
def setpoints(ctx, user : Member, points : int):
    
    if staff_role_id not in ctx.author.roles:
        return 'You are not staff.'
    
    update_points(user.id, points)
    text = 'Set {}\'s points to `{}`.'.format(user.username, points)
    
    return text

@app.command(description = 'Gets everyone\'s points')
def getall(ctx, user : Member, points : int):
    
    if staff_role_id not in ctx.author.roles:
        return 'You are not staff.'

    response = db.fetch()
    data = [tuple(i.values()) for i in response.items]
    while response.last:
        response = db.fetch(last = response.last)
        data.extend([tuple(i.values()) for i in response.items])
        
    data.sort(key = lambda x : x[0])
    
    text = '\n'.join(
        '`{}.` <@{}> - {}'.format(i, user_id, points)
        for i, (user_id, points) in enumerate(data)
    )
    
    embed = Embed(
        title = '{} entries'.format(len(data)),
        descripton = text[:4096],
        color = 0x7289da
    )
   
    return embed

@app.route('/')
def index(request, start_response, abort):
    start_response('200 OK', [])
    return ['Home'.encode('UTF-8')]

@app.route('/update_commands')
def home(request, start_response, abort):
    app.update_commands(from_inside_a_micro=True)
    start_response('200 OK', [])
    return ['updated commands'.encode('UTF-8')]
