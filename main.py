from flask import Flask, jsonify, request

app = Flask(__name__)

#Sample data
games = [
    {"id":1,"title":"Crysis", "developer":"EA"},
    {"id":2,"title":"Call of Duty", "developer":"Activision"},
    {"id":3,"title":"Red Dead Redemption", "developer":"Rockstar Games"}
]

#Get all games
@app.route('/games', methods=['GET'])
def get_games():
    return games

#Get one game
@app.route('/games/<int:game_id>', methods=['GET'])
def get_game(game_id):
    for game in games:
        if game['id'] == game_id:
            return game
        return {'error':'Game not found'}
    
#Create a new entry
@app.route('/games', methods=['POST'])
def create_game():
    new_game = {'id':len(games)+1,'title':request.json['title'], 'developer':request.json['developer']}
    games.append(new_game)
    return new_game

#Update an entry
@app.route('/games/<int:game_id>', methods=['PUT'])
def update_games(game_id):
    for game in games:
        if game['id']==game_id:
            game['title']=request.json['title']
            game['developer']=request.json['developer']
            return game
        return {'error':'Game not found'}
    
#Delete an enrty
@app.route('/games/<int:game_id>', methods=['DELETE'])
def delete_game(game_id):
    for game in games:
        if game['id']==game_id:
            return game
        return {'error': 'Game not found'}

#running the API
if __name__ == '__main__':
    app.run(debug=True)