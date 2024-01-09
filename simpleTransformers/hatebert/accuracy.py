from sklearn.metrics import f1_score, recall_score, precision_score
import pandas as pd
from simpletransformers.classification import ClassificationModel, ClassificationArgs
import numpy as np


def macro_f1(y_true, y_pred):
    return f1_score(y_true, y_pred, average='macro')




# Replace 'dataset.csv' with the path to your CSV file
file = "dataset.csv"

#read the csv without using pandas
with open(file, "r", encoding="utf-8") as f:
    data = f.readlines()
    f.close()



    model = ClassificationModel("bert", "outputs", use_cuda=True)

    for text in data:
        text= text.replace("\n", "")
        
        
        result, output = model.predict(text)
        

        logits = np.array(output[0])

        # Applying softmax to convert logits to probabilities
        probabilities = np.exp(logits) / np.sum(np.exp(logits))
        if probabilities[1] > 0.8:
            
            #add to offensive.csv
            csv = open("offensive.csv", "a", encoding="utf-8")
            csv.write(f'{text}\r')
            csv.close()
            
    
# print(eval_df["labels"].tolist())

# print(f1_score(eval_df["labels"].tolist(), result, average="macro"))


