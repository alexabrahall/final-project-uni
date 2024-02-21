from sklearn.metrics import f1_score, recall_score, precision_score
import pandas as pd
from simpletransformers.classification import ClassificationModel, ClassificationArgs


def macro_f1(y_true, y_pred):
    return f1_score(y_true, y_pred, average='macro')




train_data = pd.read_csv("eng_3_dev.tsv", encoding="utf-8", sep="\t")

train_data = train_data.drop(columns=["Unnamed: 2", "Unnamed: 3", "Unnamed: 4", "Unnamed: 5", "Unnamed: 6", "Unnamed: 7", "Unnamed: 8", "Unnamed: 9"])

train_data.columns = ["labels", "text"]

train_data["labels"] = train_data["labels"].replace("Homophobic", 1)
train_data["labels"] = train_data["labels"].replace("Non-anti-LGBT+ content", 0)
train_data["labels"] = train_data["labels"].replace("Transphobic", 1)

#swap columns
train_data = train_data[["text", "labels"]]

# split the data into train and eval
eval_df = train_data
train_df= train_data


print(train_data.head())
# print(train_df["text"].tolist())

model = ClassificationModel("roberta", "outputs", use_cuda=True)


result, output = model.predict(eval_df["text"].tolist())

print(result)
print(eval_df["labels"].tolist())

print(f1_score(eval_df["labels"].tolist(), result, average="macro"))


