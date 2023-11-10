# Cell 1
from simpletransformers.classification import ClassificationModel, ClassificationArgs
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
transformers_logger = logging.getLogger("transformers")
transformers_logger.setLevel(logging.WARNING)

# Cell 2
# Preparing train data
train_data = [
    ["Aragorn was the heir of Isildur", 1],
    ["Frodo was the heir of Isildur", 0],
]
train_df = pd.DataFrame(train_data)
train_df.columns = ["text", "labels"]

# Cell 3
# Preparing eval data
eval_data = [
    ["Theoden was the king of Rohan", 1],
    ["Merry was the king of Rohan", 0],
]
eval_df = pd.DataFrame(eval_data)
eval_df.columns = ["text", "labels"]

# Cell 4
# Optional model configuration
model_args = ClassificationArgs(num_train_epochs=10, use_multiprocessing=False, process_count=1, use_multiprocessing_for_evaluation=False, best_model_dir="outputs/best_modal", overwrite_output_dir=True)

# Cell 5
# Create a ClassificationModel
model = ClassificationModel(
    "roberta", "roberta-base", args=model_args
)

# Cell 6
# Train the model
model.train_model(train_df)

# Cell 7
# Evaluate the model
result, model_outputs, wrong_predictions = model.eval_model(eval_df)

# Cell 8
# Make predictions with the model
predictions, raw_outputs = model.predict(["Sam was a Wizard", "Frodo was the heir of Isildur"])


print(predictions)
