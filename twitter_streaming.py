#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "179791072-yByjpVlPGIPscb9Vz9WHFzr0HM7nLeGUUt2VwBRd"
access_token_secret = "tPm7XsF3pYGylMa0sqiWZeLKEBwTHdtTlE908Edy74rf0"
consumer_key = "YLLUHLZaCYv5BJyIkvgCxCNYA"
consumer_secret = "Ive9bA25xh3DfSm1kC0yuB3b1Lw632IAENncr0aXfFpxMjtRjf"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['python', 'javascript', 'ruby'])