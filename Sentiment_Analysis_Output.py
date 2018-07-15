import json

from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

from Twitter_Sentiment_Analysis import sentiment_pod as s

#consumer key, consumer secret, access token, access secret.
ckey="EbsbtI3p4ENCQ8rW8KSC47OKG"
csecret="JiMvdfVPC3rPJCnoIuo4MmgcfS4x4EF4ISGk0qYp7jtj1FGl1X"
atoken="1012259432108118018-Xn0ce09lv2PGxN5VeNYVeuHj2chfG7"
asecret="Y9IirwWSfBtD8SIZpErJjBC7Y6BVDOG9PL8Rt7aXbGCfu"



class listener(StreamListener):

	def on_data(self, data):

		all_data = json.loads(data)

		tweet = all_data["text"]
		sentiment_value, confidence = s.sentiment(tweet)
		print(tweet, sentiment_value, confidence)

		if confidence*100 >= 80:
			output = open("twitter-out.txt","a")
			output.write(sentiment_value)
			output.write('\n')
			output.close()

		return True

	def on_error(self, status):
		print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["cat"])