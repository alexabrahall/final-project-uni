import re
from tqdm import tqdm
import pandas as pd


data = open("dataset.csv", "r", encoding="utf-8").readlines()



stopwords = [
    stopword.strip()
    for stopword in open("stopwords.txt", "r", encoding="utf-8").readlines()
]


processed_data = []
for text in data:
    text = re.sub("@[A-Za-z0-9_]+", "", text)  # removing mentions
    text = re.sub("#[A-Za-z0-9_]+", "", text)  # removing hashtags
    text = re.sub(r"http\S+", "", text)  # removing http urls
    text = re.sub(r"www.\S+", "", text)  # removing www urls
    text = re.sub("[^a-z]", " ", text)  # removing non-letter characters
    text = " ".join([word for word in text.lower().split() if word not in stopwords])
    processed_data.append(text)

wordCount = {}


#counting words
for tweet in processed_data:
    for word in tweet.split():
        if word not in wordCount:
            wordCount[word] = 1
        else:
            wordCount[word] += 1


#remove any words that appear less than 100 times

for word in list(wordCount):
    if wordCount[word] < 100:
        del wordCount[word]

#sort words by frequency
wordCount = dict(sorted(wordCount.items(), key=lambda item: item[1], reverse=True))

#save wordcount to csv
wordCount_df = pd.DataFrame(wordCount.items(), columns=["Word", "Frequency"])

wordCount_df.to_csv("wordCount.csv", index=False)

#plot graph

import matplotlib.pyplot as plt

plt.bar(range(len(wordCount)), list(wordCount.values()), align="center")
plt.title("Word Frequency in Transhomophobic Tweets")
plt.xticks(range(len(wordCount)), list(wordCount.keys()))
plt.show()





