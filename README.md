Web Application to Display Trending Keywords and Sentiment Distribution Over Time About Popular Topics
======================================================================================================

Authors
-------
Umang Patel - ujp2001@columbia.edu , Karan Kaul- kak2210@columbia.edu


GitHub URL
----------
https://github.com/17patelumang/Twitter_Sentiment_Evolution-Word-Cloud


Screencast URL
--------------
http://www.screencast.com/t/ohaSgxEW


Description
-----------
This is a web application that allows the user to select a popular topic and displays:
(1) A [bubble cloud][1] which contains the most frequently occuring words within the topic as bubbles, each bubble's size is determined by the frequency of the keyword occuring within the topic.
(2) A word cloud which displays the most frequently occuring keywords within the selected topic.
(3) A graph which shows the distribution of sentiment about the specified topic.

As the web page is requested, a connection is established between the client and server. The user may navigate between three webpages which present the bubble cloud, word cloud or sentiment distribution over time as specified by the user.
The data requested by the user is dependant on the topic selected by the user using the drop down box.


Components & Flow
-----------------
### 1. Python script to acquire tweets ###  
In addition to the tweet dataset provided, tweets are downloaded from twitter using the Twitter streaming API filtered by keyword and language (english). The tweet content (i.e. the tweet text) is saved within a text file for all the tweets.

### 2. Generating popular topics ###
The dataset containing all the tweets is processed using ***Amazon's Elastic Map/Reduce*** to generate the most popular topics using a word count. Words below a certain threshold size and common words are ignored for topic selection. To present diverse information, varied topics were selected among the most frequently occuring topics.

### 3. Trending words within topics ###
Returning to the entire dataset, subsets of data are created which comprise of the tweets which contain each topic. A word count is carried out on the subsets of data to extract most frequently occuring keywords within a topic. Words below a certain threshold size are ignored and the result of the filtered most frequently occuring words are considered the trending words within a topic. The most frequent selected words and their frequency is saved as a comma-separated file for the bubble cloud and word cloud.

### 4. Sentiment Dictionary ###
We create dictionoary of words each having a sentiment score with it by using words from [AFFINN][2] & using words from [UIC][3] repo and also using TextBlob python library. Combining all three gives us dictionary of all positive and negative words each having a sentiment score.

### 5. Sentiment distribution over time regarding a topic ###
From the subsets of data for a single topic (as described in the previous step), we assume tweets about a single topic are evenly distributed between April 21st 2014 (20:00) and May 1st (12:00) as date/time information about each tweet is not present. Based on a [dictionary of positive and negative words][2,3], we can generate the sentiment regarding each tweet within a topic as positive, negative or neutral. We then generate for each topic the percentage of positive tweets and negative tweets for 8 hour time slots distributed between the aforementioned dates. This data is stored as a tab-separated file per topic containing two entries for each time slot, the percentage of positive and percentage of negative tweets.

### 6. Web Application ###
This is the primary web application built in HTML/CSS/JavaScript and accessed by the client which as mentioned in the description accesses the requested data from the text files and sends it to the client.


Libraries/SDKs/APIs
-------------------
### 1. Twitter API ###
Tweets and their metadata regarding certain keywords are downloaded using the Twitter streaming API.

### 2. D3 Cloud.js ###
The word cloud is generated using this library, allows customization of the word cloud such as font type, size, etc.

### 3. NVD3.js ###
The stacked bar graph which presents the distribution of the sentiment over time of the topic is generated using this library.

### 4. D3.js ###
Used in conjunction with the previous two libraries to customize general aspects of the word cloud and sentiment distribution over time graph. 

### 5. Python Libraries ###

(1) TextBlob - A python library for simplified processing of text.

(2) collections - Provides high performance alternatives to Python's datatypes

(3) sys - Provides access to parameters maintained by the interpreter

(4) os - Provides functionality that varies based on operating system

(5) re - Provides regular expression related operations

(6) operator - Efficient operations corresponding to Python operators

(7) glob - Finds pathnames matching a specified pattern

(8) random - Generates pseudo-random numbers

(9) datetime - Functions related to date and time

(10) matplotlib.pyplot - Plotting functionality similar to that provided by MATLAB

(11) wordcloud - Functionality to generate word clouds

(12) heapq - Implementation of the heap queue algorithm

Steps to run code
-----------------

__Python Script__

(1) Provide the twitter API keys to the Python script

(2) run "python twitter_stream.py".

__Application__

(1) The HTML/CSS/JavaScript files must be downloaded in the current structure, additionally, the data files as described above must be provided within a folder called 'Data'.

(2) The application can be deployed on a server running Tomcat 6


Bonus (Sentiment Distribution Over Time)
--------------------------------
The sentiment distribution over time has been plotted using D3.js and NVD3.js

Citations
---------
[1]: http://github.com/vlandham/bubble_cloud (Bubble cloud visualization, Copyright by Jim Vallandingham, Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php)

[2]: http://www2.imm.dtu.dk/pubdb/views/publication_details.php?id=6010 (F. Å. Nielsen, AFINN, Informatics and Mathematical Modelling, Technical University of Denmark, 2011)

[3]: http://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html (Bing Liu, Minqing Hu and Junsheng Cheng."Opinion Observer: Analyzing and Comparing Opinions on the Web." Proceedings of the 14th International World Wide Web conference (WWW-2005), May 10-14, 2005, Chiba, Japan.)

(1): http://github.com/vlandham/bubble_cloud (Bubble cloud visualization, Copyright by Jim Vallandingham, Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php)

(2): http://www2.imm.dtu.dk/pubdb/views/publication_details.php?id=6010 (F. Å. Nielsen, AFINN, Informatics and Mathematical Modelling, Technical University of Denmark, 2011)

(3): http://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html (Bing Liu, Minqing Hu and Junsheng Cheng."Opinion Observer: Analyzing and Comparing Opinions on the Web." Proceedings of the 14th International World Wide Web conference (WWW-2005), May 10-14, 2005, Chiba, Japan.)
