import unicodedata


class TweetDivider:

    def __init__(self, tweets, wordsFiles):
        self.__tweets = tweets
        self.__wordsFiles = wordsFiles

    def clasifyAllTweets(self):
        cosa = 0
        for tweet in self.__tweets.getAllData():
            text = unicodedata.normalize('NFKD', tweet[3]).encode('ASCII', 'ignore').decode("utf-8").lower()
            for wordFiles in self.__wordsFiles:
                for words in wordFiles.getAllLines():
                    if text.find(words.lower()) is not -1:
                        cosa += 1

        return cosa