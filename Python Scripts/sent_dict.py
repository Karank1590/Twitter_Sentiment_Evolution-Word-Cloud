import os
from textblob import TextBlob
import sys
import re
import glob
import random
from collections import defaultdict
import operator

p=dict(defaultdict(float))
n=dict(defaultdict(float))


# Authors: Umang Patel - ujp2001 , Karan Kaul - kak2210
# This script is used combine all positive and negative words from different sources each having a sentiment score with them to dump into common file by removing duplicates 


#to run : time python sent_dict.py

def sent_dict():
	os.system("time python AFFIN_WORDS.py AFFIN_words/AFINN-111.txt")
	os.system("time python AFFIN_WORDS.py AFFIN_words/AFINN-96.txt")
	os.system("time python UIC.py UIC_WORDS/positive-words.txt")
	os.system("time python UIC.py UIC_WORDS/negative-words.txt")
	os.system("time python sentiment.py tweet_words")


	with open("/Users/umang/Documents/assi3_cloud/POSITIVE.txt") as f:
		for line in f:

			if line != "\n":
				l1=line.strip("\n").split(" ")

				if(l1[0] not in p):
					p[str(l1[0])]=l1[1]
	
	f.close()			
	print len(p)		


	pf = open("/Users/umang/Documents/assi3_cloud/COMBINE_POSITIVE.txt", "a+")
	for k ,v in sorted(p.items(), key=operator.itemgetter(0)):
		#print k ,v
		pf.write(k+" "+str(v)+"\n")
	pf.close()	

	with open("/Users/umang/Documents/assi3_cloud/NEGATIVE.txt") as f:
		for line in f:

			if line !="\n":
				l1=line.strip("\n").split(" ")
				#print l1

				if(l1[0] not in n):
					n[str(l1[0])]=l1[1]

	f.close()
	print len(n)


	nf = open("/Users/umang/Documents/assi3_cloud/COMBINE_NEGATIVE.txt", "a+")
	for k ,v in sorted(n.items(), key=operator.itemgetter(0)):
		#print k ,v
		nf.write(k+" "+str(v)+"\n")
	nf.close()


if __name__ == "__main__":
	sent_dict()