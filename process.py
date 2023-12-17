import pandas as pd


# get the data from the .csv file
train_data = pd.read_csv("eng_3_train.tsv", sep="\t")

train_data = train_data.drop(columns=["Unnamed: 2", "Unnamed: 3", "Unnamed: 4", "Unnamed: 5", "Unnamed: 6", "Unnamed: 7", "Unnamed: 8", "Unnamed: 9", "Unnamed: 10", "Unnamed: 11", "Unnamed: 12", "Unnamed: 13", "Unnamed: 14", "Unnamed: 15"])





train_data.columns = ["labels", "text"]

train_data["labels"] = train_data["labels"].replace("Homophobic", 1)
train_data["labels"] = train_data["labels"].replace("Non-anti-LGBT+ content", 0)

#swap columns
train_data = train_data[["text", "labels"]]

print(train_data.head())