import pandas as pd


# get the data from the .csv file
train_data = pd.read_csv("olid-training-v2.0.csv", sep=",", encoding="utf-8")


# remove the unnecessary columns
train_data = train_data.drop(columns=["example_no", "annotator_id", "conv_id", "prev_agent", "prev_user", "agent", "bot", "is_abuse.1","is_abuse.0","is_abuse.-1", "is_abuse.-2", "is_abuse.-3","type.ableism", "type.intellectual","type.sexist", "type.sex_harassment","target.generalised", "target.individual", "target.system", "direction.explicit", "direction.implicit", "type.racist"])

print(train_data.head())