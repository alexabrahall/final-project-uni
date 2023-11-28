import numpy as np
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re



csv_data = open("dataset.csv", "r", encoding="utf-8").readlines()



stopwords = [
    stopword.strip()
    for stopword in open("stopwords.txt", "r", encoding="utf-8").readlines()
]

processed_data = []

for text in csv_data:
    text = re.sub("@[A-Za-z0-9_]+", "", text)  # removing mentions
    text = re.sub("#[A-Za-z0-9_]+", "", text)  # removing hashtags
    text = re.sub(r"http\S+", "", text)  # removing http urls
    text = re.sub(r"www.\S+", "", text)  # removing www urls
    text = re.sub("[^a-z]", " ", text)  # removing non-letter characters
    text = " ".join([word for word in text.lower().split() if word not in stopwords])
    processed_data.append(text)



wc = WordCloud(max_font_size=100).generate("".join(processed_data))
wc.background_color = "white"
plt.figure()
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()

