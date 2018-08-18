from tweepy.streaming import StreamListener
import json


class StreamListenerCeuma(StreamListener):

    def on_data(self, raw_data):
        json_data = json.loads(raw_data)
        print(json_data['text'])
        return True

    def on_error(self, status_code):
        print(status_code)
