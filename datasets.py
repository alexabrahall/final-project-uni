import pandas as pd

#convabuse
train_data = pd.read_csv("convabuse2.csv", sep=",", encoding="utf-8")


# remove the unnecessary columns
train_data = train_data.drop(columns=["example_no", "annotator_id", "conv_id", "prev_agent", "prev_user", "agent", "bot", "is_abuse.1","is_abuse.0","is_abuse.-1", "is_abuse.-2", "is_abuse.-3","type.ableism", "type.intellectual","type.sexist", "type.sex_harassment","target.generalised", "target.individual", "target.system", "direction.explicit", "direction.implicit", "type.racist"])

for index, row in train_data.iterrows():
    if row["type.transphobic"] == 1:
        train_data.at[index, "type.homophobic"] = 1
   

# rename the columns
train_data = train_data.drop(columns=["type.transphobic"])
train_data.columns = ["text", "labels"]
#split the data into train and eval
train_df = train_data
eval_df = train_data

#HTDM
train_data = pd.read_csv("eng_3_dev2.tsv", encoding="utf-8", sep="\t")

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

#convabuse LLM
train_data = pd.read_csv("convabuse2.csv", sep=",", encoding="utf-8")


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
eval_df = train_data[12752:]



template = """Comments that include homophobic or transphobic remarks, whether overt or implied, are considered offensive. This encompasses derogatory language, threats, and expressions that disrespect or invalidate someone's sexual orientation or gender identity. Conversely, comments that are respectful and do not contain homophobic or transphobic content are not considered offensive.
Here are 3 examples of comments:
"u r devil follower not god"
"Shame on u hell is waiting hell repent or perish judgement is near"
"I don't support this because it's against nature."
"Shame on u hell is waiting hell repent or perish judgement is near	"
"I don't support this because it's against nature."
Question: {question}
Answer:"""