# Cell 1
from simpletransformers.classification import ClassificationModel, ClassificationArgs
import pandas as pd
import logging
from sklearn.metrics import accuracy_score,f1_score


#get the data from the .tsv file
train_data = pd.read_csv("olid-training-v2.0.csv", sep=",", encoding="utf-8")


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
model_args = ClassificationArgs(num_train_epochs=3, use_multiprocessing=False, process_count=2, use_multiprocessing_for_evaluation=False, best_model_dir="outputs/best_modal", overwrite_output_dir=True, save_best_model=True, wandb_project="Final Project",wandb_kwargs={"name": "roBERTa"})

# # Cell 5
# # Create a ClassificationModel
model = ClassificationModel(
    "roberta", "roberta-base", args=model_args, num_labels=2
)

# # Cell 6
# Train the model
model.train_model(train_df, acc=accuracy_score)

# # Cell 7
# # Evaluate the model
result, model_outputs, wrong_predictions = model.eval_model(eval_df)
print(result)

# Cell 8
# Make predictions with the model
predictions, raw_outputs = model.predict(["@USER Grateful Trump doesn’t have a dog in the White House. He is a cruel man.", "Hello, how are you today?"])


print(predictions)
