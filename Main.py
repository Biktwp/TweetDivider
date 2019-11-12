from FileManager import *
from TweetDivider import *

if __name__ == '__main__':
    tweets = FileManager("./Files/pruebas.tsv", "\t")
    words = FileManager("./Files/PP.txt", "\t")

    aux = [words]

    tweetDivider = TweetDivider(tweets, aux)


    print(tweetDivider.clasifyAllTweets())

