import sys
import re
import glob

#  Authors: Umang Patel - ujp2001 , Karan Kaul - kak2210
#  This script is used to convert words from AFFIN dataset to score in range [-1,1] and dump into a File having format "words score"


# to run : time python AFFIN_WORDS.py AFFIN_words/AFINN-96.txt

def affin():

	pos= open("/Users/umang/Documents/assi3_cloud/POSITIVE.txt", "a+")
	neg= open("/Users/umang/Documents/assi3_cloud/NEGATIVE.txt", "a+")

	with open(sys.argv[1]) as f:
		for line in f:
			words=line.split("\t")[0].strip("\t\n")
			sentiment=int(line.split("\t")[1])
		
			if int(sentiment)>0:
				pos.write(words+" "+str(sentiment/float(5))+"\n")
			elif int(sentiment)<0:
				neg.write(words+" "+str(sentiment/float(5))+"\n")	

	pos.close()
	neg.close()	

if __name__ == "__main__":
	affin()