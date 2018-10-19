from flask import Flask, jsonify, Blueprint, request
from flask_restful import Resource, Api, reqparse, abort
import json
import datetime

# user = [{
#     "username": "John",
#     "email": "john@haha.com",
#     "password": "Hahaha123",
#     "fullname": "John rukmana"
# },
# {
#     "username": "jeff",
#     "email": "jeff@haha.com",
#     "password": "Hahaha123",
#     "fullname": "John rukmana"
# }]

# tweet = [{
#     "email": "john@haha.com",
#     "tweet": "Ini ceritanya tweet Twitter yah"
# },
# {
#     "email": "jeff@haha.com",
#     "tweet": "Ini ceritanya tweet Twitter yah"
# }]



user = []
tweet = []


# with open('user.json', 'w') as outfile:  
#     json.dump(user, outfile)

# with open('tweet.json', 'w') as outfile:  
#     json.dump(tweet, outfile)

with open('user.json') as user_file:
    user = json.load(user_file)

with open('tweet.json') as tweet_file:
    tweet = json.load(tweet_file)
    
def tambahUser():
    with open('user.json', 'w') as outfileuser:
            json.dump(user, outfileuser)
            outfileuser.close()

def tambahTweet():
    with open('tweet.json', 'w') as outfiletweet:
            json.dump(tweet, outfiletweet)
            outfiletweet.close()


class allUser(Resource):
    def get(self):
        return user

class allTweet(Resource):
    def get(self):
        return tweet

class login(Resource):
    def post(self):
        email = request.json["email"]
        password = request.json["password"]

        for data in user:
            if data['email'] == email and data['password'] == password:
                return data, 200
            elif data['email'] == email and data['password'] != password:
                return "PASSWORD SALAH", 400
        return "EMAIL BELUM TERDAFTAR", 404
        

def emailTerdaftar(mail):
    for data in user:
        if data['email'] == mail:
            abort(400, message = "email telah terdaftar")

def userTerdaftar(name):
    for data in user:
        if data['username'] == name:
            abort(400, message = "username telah terdaftar")

class Signup(Resource):
    def __init__(self):
            self.reqparse = reqparse.RequestParser()
            self.reqparse.add_argument(
                "email",
                help = "Email wajib diisi",
                required = True,
                location = ["json"]
            )
            self.reqparse.add_argument(
                "username",
                help = "username wajib diisi",
                required = True,
                location = ["json"]
            )
            self.reqparse.add_argument(
                "password",
                help = "password wajib diisi",
                required = True,
                location = ["json"]
            )
            self.reqparse.add_argument(
                "fullname",
                help = "fullname wajib diisi",
                required = True,
                location = ["json"]
            )
            super().__init__()

    def post(self):
        args = self.reqparse.parse_args()
        emailTerdaftar(request.json['email'])
        userTerdaftar(request.json['username'])
        user.append(request.json)
        tambahUser()        
        return "Akun Berhasil di Buat", 201

class Tweet(Resource):
     def __init__(self):
            self.reqparse = reqparse.RequestParser()
            self.reqparse.add_argument(
                "email",
                help = "Email wajib diisi",
                required = True,
                location = ["json"]
            )
            
            self.reqparse.add_argument(
                "tweet",
                help = "tweet tidak boleh kosong",
                required = True,
                location = ["json"]
            )
            super().__init__()

     def post(self):
         data = request.json
         time = str(datetime.datetime.now())
         tmp = {}
         tmp["time"] = time
         req = data.copy()
         req.update(tmp)
         args = self.reqparse.parse_args()
         tweet.append(req)
         tambahTweet()
         return "tweet telah dibuat",201

     def delete(self):
        email = request.json["email"]
        twit = request.json["tweet"]

        for index in range(len(tweet)):
            if tweet[index]['email'] == email and tweet[index]['tweet'] == twit:
                tweet.pop(index)
                tambahTweet()
                return "Tweet telah terhapus", 200
        return "Tweet tidak ditemukan", 404

     def put(self):
         email = request.json["email"]
         oldTwit = request.json["old tweet"]
         newTwit = request.json["new tweet"]
         
         for index in range(len(tweet)):
             if tweet[index]['email'] == email and tweet[index]['tweet'] == oldTwit:
                 tweet[index]['tweet'] = newTwit
                 tweet[index]['time'] = str(datetime.datetime.now())
                 tambahTweet()
                 return "tweet telah diubah", 201
             return "tweet tidak ada", 400
    
     def get(self):
        tweetList = []
        email = request.json['email']
        for twits in tweet:
            if twits['email'] == email:
                tweetList.append(twits['tweet'])
        return tweetList, 200







tweeps_api = Blueprint('resources/tweeps', __name__)
api = Api(tweeps_api)
api.add_resource(allUser, 'allUser')
api.add_resource(allTweet,'allTweet')
api.add_resource(login, 'login')
api.add_resource(Signup, 'Signup')
api.add_resource(Tweet, 'Tweet')
