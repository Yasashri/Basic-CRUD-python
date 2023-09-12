from flask import Flask, jsonify, request

app = Flask(__name__)

#Sample data
games = [
    {"id":1,"title":"Crysis", "developer":"EA"},
    {"id":2,"title":"Call of Duty", "developer":"Activision"},
    {"id":3,"title":"Red Dead Redemption", "developer":"Rockstar Games"}
]

#Get all games
app.route('/games', setMethod=['GET'])
def get_games():
    return games

#running thid API
if __name__ == '__main__':
    app.run(debug=True)