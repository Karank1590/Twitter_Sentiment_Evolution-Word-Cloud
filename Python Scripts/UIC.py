from textblob import TextBlob
import sys
import re
import glob
import random


#  Authors: Umang Patel - ujp2001 , Karan Kaul - kak2210
#  This script is used to convert words from UIC dataset to score in range [-1,1] and dump into a File having format "words score"

# To be run simultaneously for positing and negative
# to run : time python UIC.py UIC_WORDS/positive-words.txt

def senti():

	i_p=sys.argv[1]
	f_open=((i_p.split("/")[-1]).split("-")[0]).upper()
	ff_file="/Users/umang/Documents/assi3_cloud/"+f_open+".txt"
	ff= open(ff_file, "a+")
	

	with open(i_p) as f:
		for line in f:
			words=line.split("\t")[0].strip("\n\t")

			#print words

			word_senti = TextBlob(str(words))
			if(word_senti.sentiment.polarity==0):

				if(f_open=="POSITIVE"):
					ff.write(words+" "+str(random.uniform(0.5, 1.0))+"\n")
				if(f_open=="NEGATIVE"):	
					ff.write(words+" "+str(random.uniform(-0.5, -1.0))+"\n")
			else:	
				ff.write(words+" "+str(word_senti.sentiment.polarity)+"\n")



	ff.close()			



if __name__ == "__main__":
	senti()