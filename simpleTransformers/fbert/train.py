# Cell 1
from simpletransformers.classification import ClassificationModel, ClassificationArgs
import pandas as pd
import logging
from sklearn.metrics import accuracy_score,f1_score


#get the data from the .tsv file
train_data = pd.read_csv("olid-training-v1.0.tsv", sep="\t")

#remove the unnecessary columns
train_data = train_data.drop(columns=["id", "subtask_b", "subtask_c"])
#rename the subtask_a to an int 
train_data["subtask_a"] = train_data["subtask_a"].replace("OFF", 1)
train_data["subtask_a"] = train_data["subtask_a"].replace("NOT", 0)
train_data.columns = ["text", "labels"]

#remove all the @USER tags
train_data["text"] = train_data["text"].str.replace("@USER", "")
#remove all the URL tags
train_data["text"] = train_data["text"].str.replace("URL", "")
#remove all the hashtags
train_data["text"] = train_data["text"].str.replace("#", "")   

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
model_args = ClassificationArgs(num_train_epochs=25, use_multiprocessing=False, process_count=2, use_multiprocessing_for_evaluation=False, best_model_dir="outputs/fbert", overwrite_output_dir=True, save_best_model=True)

# # Cell 5
# # Create a ClassificationModel
model = ClassificationModel(
    "bert", "diptanu/fBERT", args=model_args, num_labels=2
)

# Cell 6
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
