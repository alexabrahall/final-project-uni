# Cell 1
from simpletransformers.classification import ClassificationModel, ClassificationArgs
import pandas as pd
import logging
from sklearn.metrics import accuracy_score, f1_score


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
train_df = train_data


logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)

# # Cell 2
# # Preparing train data
# train_data = [
#     ["Aragorn was the heir of Isildur", 1],
#     ["Frodo was the heir of Isildur", 0],
# ]
# train_df = pd.DataFrame(train_data)
# train_df.columns = ["text", "labels"]

# # Cell 3
# # Preparing eval data
# eval_data = [
#     ["Theoden was the king of Rohan", 1],
#     ["Merry was the king of Rohan", 0],
# ]
# eval_df = pd.DataFrame(eval_data)
# eval_df.columns = ["text", "labels"]

# # Cell 4
# # Optional model configuration
model_args = ClassificationArgs(
    num_train_epochs=3,
    use_multiprocessing=False,
    process_count=2,
    use_multiprocessing_for_evaluation=False,
    best_model_dir="outputs/bertweet_base",
    overwrite_output_dir=True,
    save_best_model=True,
    wandb_project="Final Project",
    wandb_kwargs={"name": "BERTweet"},
)

# # Cell 5
# # Create a ClassificationModel
model = ClassificationModel("auto", "vinai/bertweet-base", args=model_args)

# Cell 6
# Train the model
model.train_model(train_df, acc=accuracy_score)





# Cell 8
# Make predictions with the model
predictions, raw_outputs = model.predict(
    [
        "@USER Grateful Trump doesn’t have a dog in the White House. He is a cruel man.",
        "Hello, how are you today?",
    ]
)


print(predictions)
