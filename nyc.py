
import couchdb
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json


###API ########################
ckey = "l74Qtm7NRcByUC8flRUpAgLfn"
csecret = "Dpbw43cRn8Go2Di0YHYG9ZtCam1nHw2pcgnh67ONZn4Mf0mahq"
atoken = "1574277428-7ANeKTU7WsNu7Vn7kh2XPigUGIjXuHn043GGRGH"
asecret = "K9nzrVDbEAuJ6Beeiubri0w9EAZ0l9VUrPFJOdrrLGg28"
#####################################

class listener(StreamListener):
    
    def on_data(self, data):
        dictTweet = json.loads(data)
        try:
            
            dictTweet["_id"] = str(dictTweet['id'])
            doc = db.save(dictTweet)
            print ("SAVED" + str(doc) +"=>" + str(data))
        except:
            print ("Already exists")
            pass
        return True
    
    def on_error(self, status):
        print (status)
        
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())

'''========couchdb'=========='''
server = couchdb.Server('http://chantal:12345@localhost:5984/')  #('http://115.146.93.184:5984/')
try:
    db = server.create('newyork2')
except:
    db = server['newyork2']
    
'''===============LOCATIONS=============='''    

#twitterStream.filter(locations=[-79.76,40.48,-71.8,45.02])  
twitterStream.filter(track=['NYC'])