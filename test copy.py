
data = open("dataset.csv", "r", encoding="utf-8").readlines()

file = open("convabuse.csv", "a", encoding="utf-8")

for line in data:
    line = line.replace("\n", "")
    
    if line == "":
        continue
    file.write(f"0,Annotator 1,123,x,x,x,{line},0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0\n")
    