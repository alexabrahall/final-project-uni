from langchain import HuggingFacePipeline
from langchain import PromptTemplate,  LLMChain
from transformers import AutoTokenizer, pipeline
import pandas as pd
import torch



model = "tiiuae/falcon-7b-instruct" #tiiuae/falcon-40b-instruct

tokenizer = AutoTokenizer.from_pretrained(model)

pipeline = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
)

llm = HuggingFacePipeline(pipeline=pipeline, model_kwargs={'temperature':0})
template = """Comments containing any form of non-acceptable language (profanity) or a targeted offense, which can be veiled or direct are offensive comments. This includes insults, threats, and postscontaining profane language or swear words. Comments that do not contain offense or profanity are not offensive.
Question: {question}
Answer:"""
prompt = PromptTemplate(template=template, input_variables=["question"])

llm_chain = LLMChain(prompt=prompt, llm=llm)

test = open("dataset.csv", "r", encoding="utf-8").readlines()

csv = open("falcon_predictions.csv", "a", encoding="utf-8")
csv.write("Tweet,Label\n")

final_predictions = []
i = 0
for  row in test:
    row = row.replace("\n", "")
    question = "Is this comment offensive or not? Comment: " + row
    response = llm_chain.run(question)

    print(f"The model predicted {response} for the comment: {row} - {i} of {len(test)}")
    
    if "Yes" in response:
        print("The model predicted that the comment is offensive")
        csv.write(f'{row},1\n')
    else:
        print("The model predicted that the comment is not offensive")
        csv.write(f'{row},0\n')

    i+=1


# test['predictions'] = final_predictions




