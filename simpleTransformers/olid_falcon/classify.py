from langchain import HuggingFacePipeline
from langchain import llms, prompts, chains
import langchain
from transformers import AutoTokenizer, pipeline
import pandas as pd
import torch
from sklearn.metrics import f1_score, recall_score, precision_score


model = "mistralai/Mistral-7B-Instruct-v0.2" #tiiuae/falcon-40b-instruct

tokenizer = AutoTokenizer.from_pretrained(model)

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
eval_df = train_data[628:]
train_df= train_data[628:]

pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
    max_length=128,
    
)

llm = langchain.llms.huggingface_pipeline.HuggingFacePipeline(pipeline=pipeline, model_kwargs={'temperature':0, 'max_tokens':200})
template = """Comments that include homophobic or transphobic remarks, whether overt or implied, are considered offensive. This encompasses derogatory language, threats, and expressions that disrespect or invalidate someone's sexual orientation or gender identity. Conversely, comments that are respectful and do not contain homophobic or transphobic content are not considered offensive.

Question: {question}
Answer:"""

# template = "{question}"
prompt = prompts.PromptTemplate(template=template, input_variables=["question"])

llm_chain = chains.LLMChain(prompt=prompt, llm=llm)



final_predictions = []
i = 0
for  row in eval_df["text"].tolist():
    row = row.replace("\n", "")
    question = "Is this comment homotransphobic or not? Please only answer with 'Yes' or 'No'. Comment: " + row
    response = llm_chain.run(question)

    print(f"The model predicted {response} for the comment: {row} - {i}")
    
    if "Yes" in response:
        final_predictions.append(1)
    else:
        final_predictions.append(0)

    i+=1

print(f1_score(eval_df["labels"].tolist(), final_predictions, average="macro"))


# test['predictions'] = final_predictions




