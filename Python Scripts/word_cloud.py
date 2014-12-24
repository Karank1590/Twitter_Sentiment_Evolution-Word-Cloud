from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import random
from collections import defaultdict
import operator


#  Authors: Umang Patel - ujp2001 , Karan Kaul - kak2210
#  This script is create jpeg of word cloud for each topic. Here below "topic" variable is to be replaced.

topic="android"
d = path.dirname(__file__)

tt=dict(defaultdict(int))
top_words=100
counter=0
path_file='/Users/umang/Documents/assi3_cloud/tweet_words/'+topic+'/M_'+topic+'.txt'
text_ori = open(path.join(d, path_file)).read().split("\n")[:-1]





sentence=""
for v in text_ori:
	vtemp=v.split()
	tt[str(vtemp[0])]=int(vtemp[1])

#print sentence

file_csv=topic+".csv"
f = open(file_csv, "w+")
f.write("name,count\n")
for k,v in sorted(tt.items(), key=lambda x: x[1],reverse=True):
	#print k,v
	if(counter<=top_words and (str(k)!=str(topic)) and (len(str(k))<=8) and (len(str(k))>=4)) and (str(k)!=str("https")) and (str(k)!=str("http")) and (str(k)!=str("follow")):
		f.write(str(k)+","+str(v)+"\n")
		for ii in range(int(v)):
			sentence+=str(k)+" "
		counter+=1
	
f.close()		

wordcloud = WordCloud(background_color="white",font_path='/Users/umang/Library/Fonts/Verdana.ttf',width=1280, height=720).generate(sentence)

plt.figure(figsize=(16,9))
plt.imshow(wordcloud)

plt.axis("off")
fig1 = plt.gcf()
plt.draw()
image_name=topic+'_wordcloud.png'
fig1.savefig(image_name, bbox_inches='tight')








