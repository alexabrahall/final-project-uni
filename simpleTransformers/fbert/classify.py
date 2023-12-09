from simpletransformers.classification import ClassificationModel, ClassificationArgs
import pandas as pd
import re


data = open("dataset.csv", "r", encoding="utf-8").readlines()



stopwords = [
    stopword.strip()
    for stopword in open("stopwords.txt", "r", encoding="utf-8").readlines()
]





#load the model
model = ClassificationModel("bert", "outputs", use_cuda=True)

#predict the labels and write to csv

csv = open("fbert_predictions2.csv", "a", encoding="utf-8")
csv.write("Tweet,Label\n")

i=0
for text in data:
    print(f"Predicting tweet {i} of {len(data)}")
    if text == "\n":
        i+=1
        continue
    original_text = text.replace("\n", "")
    text = re.sub("@[A-Za-z0-9_]+", "", text)  # removing mentions
    text = re.sub("#[A-Za-z0-9_]+", "", text)  # removing hashtags
    text = re.sub(r"http\S+", "", text)  # removing http urls
    text = re.sub(r"www.\S+", "", text)  # removing www urls
    text = re.sub("[^a-z]", " ", text)  # removing non-letter characters
    #remove the \n 

    result, output= model.predict([text])

    csv.write(f'{original_text},{result[0]}\n')

    i+=1


