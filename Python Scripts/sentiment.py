import sys
import re
import glob
from textblob import TextBlob

#  Authors: Umang Patel - ujp2001 , Karan Kaul - kak2210
#  This script is used to get sentiment of words using "Textblob" library

# To run time python sentiment.py tweet_words


def senti():

	pos= open("/Users/umang/Documents/assi3_cloud/POSITIVE.txt", "a+")
	neg= open("/Users/umang/Documents/assi3_cloud/NEGATIVE.txt", "a+")

	path=sys.argv[1]+"/"
	topics=["android/M_android.txt","twitter/M_twitter.txt","justinbieber/M_justinbieber.txt","ipad/M_ipad.txt","internet/M_internet.txt","pink/M_pink.txt","snapchat/M_snapchat.txt","youtube/M_youtube.txt","chocolate/M_chocolate.txt","facebook/M_facebook.txt","coffee/M_coffee.txt","allah/M_allah.txt","disney/M_disney.txt","apple/M_apple.txt","madrid/M_madrid.txt","christmas/M_christmas.txt"]

	for topic in topics:

		with open(path+topic) as f:
			for line in f:
				words=line.split("\t")[0]

				if (len(str(words))<=8) and (len(str(words))>=4) and (str(words)!=str("https")) and (str(words)!=str("http")) and (str(words)!=str("follow")):
					words=words.strip("\n\t")
					word_senti = TextBlob(str(words))

					if(word_senti.sentiment.polarity >0):
						#print words+"\t"+str(word_senti.sentiment.polarity)+"\n"
						pos.write(words+" "+str(word_senti.sentiment.polarity)+"\n")
					elif(word_senti.sentiment.polarity <0):
						#print words+"\t"+str(word_senti.sentiment.polarity)+"\n"
						neg.write(words+" "+str(word_senti.sentiment.polarity)+"\n")
	
	pos.close()
	neg.close()

if __name__ == "__main__":
	senti()