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
#running the API
if __name__ == '__main__':
    app.run(debug=True)