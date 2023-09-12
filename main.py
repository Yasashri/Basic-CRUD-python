from flask import Flask, jsonify, request

app = Flask(__name__)

#Sample data
games = [
    {"id":1,"title":"Crysis", "developer":"EA"},
    {"id":2,"title":"Call of Duty", "developer":"Activision"},
    {"id":3,"title":"Red Dead Redemption", "developer":"Rockstar Games"}
]
