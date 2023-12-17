from sklearn.metrics import f1_score, recall_score, precision_score
import pandas as pd
from simpletransformers.classification import ClassificationModel, ClassificationArgs


def macro_f1(y_true, y_pred):
    return f1_score(y_true, y_pred, average='macro')



train_data = pd.read_csv("convabuse.csv", sep=",", encoding="utf-8")


# remove the unnecessary columns
train_data = train_data.drop(columns=["example_no", "annotator_id", "conv_id", "prev_agent", "prev_user", "agent", "bot", "is_abuse.1","is_abuse.0","is_abuse.-1", "is_abuse.-2", "is_abuse.-3","type.ableism", "type.intellectual","type.sexist", "type.sex_harassment","target.generalised", "target.individual", "target.system", "direction.explicit", "direction.implicit", "type.racist"])

for index, row in train_data.iterrows():
    if row["type.transphobic"] == 1:
        train_data.at[index, "type.homophobic"] = 1
   

# rename the columns
train_data = train_data.drop(columns=["type.transphobic"])
train_data.columns = ["text", "labels"]
#split the data into train and eval
train_df = train_data[:10000]
eval_df = train_data[10000:]

# print(train_df["text"].tolist())

model = ClassificationModel("auto", "outputs", use_cuda=True)


result, output = model.predict(eval_df["text"].tolist())

print(result)
print(eval_df["labels"].tolist())

print(f1_score(eval_df["labels"].tolist(), result, average="macro"))


