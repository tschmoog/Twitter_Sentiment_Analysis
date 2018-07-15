from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
#import sentiment_pod as s

import os
cwd = os.getcwd()
print (cwd)

#consumer key, consumer secret, access token, access secret.
ckey="EbsbtI3p4ENCQ8rW8KSC47OKG"
csecret="JiMvdfVPC3rPJCnoIuo4MmgcfS4x4EF4ISGk0qYp7jtj1FGl1X"
atoken="1012259432108118018-Xn0ce09lv2PGxN5VeNYVeuHj2chfG7"
asecret="Y9IirwWSfBtD8SIZpErJjBC7Y6BVDOG9PL8Rt7aXbGCfu"

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["cat"])
