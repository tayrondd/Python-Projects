import pandas as pd

df = pd.read_csv("./data/french_words.csv")
word_list = df.to_dict(orient="records")

print(df)
print(word_list)
word = word_list[0]
print(word["French"])