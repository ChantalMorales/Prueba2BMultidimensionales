import pymongo
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


ckey = "l74Qtm7NRcByUC8flRUpAgLfn"
csecret = "Dpbw43cRn8Go2Di0YHYG9ZtCam1nHw2pcgnh67ONZn4Mf0mahq"
atoken = "1574277428-7ANeKTU7WsNu7Vn7kh2XPigUGIjXuHn043GGRGH"
asecret = "K9nzrVDbEAuJ6Beeiubri0w9EAZ0l9VUrPFJOdrrLGg28"


class listener(StreamListener):

    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            dictTweet["_id"] = str(dictTweet['id'])
            doc = mycol.insert_one(dictTweet)
            print("SAVED" + str(doc) + "=>" + str(data))
        except:
            print("Already exists")
            pass
        return True

    def on_error(self, status):
        print(status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''Mmongo'''

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb=myclient["bdd3"]
mycol = mydb["trump"]

'''===============LOCATIONS=============='''


twitterStream.filter(track=['Donald Trump'])

