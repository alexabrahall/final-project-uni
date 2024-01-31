
data = open("dataset.csv", "r", encoding="utf-8").readlines()

file = open("eng_3_dev2.tsv", "a", encoding="utf-8")

for line in data:
    line = line.replace("\n", "")
    line = line.replace('"', "")
    
    if line == "":
        continue
    file.write("Homophobic\t" + line + "\n")
    