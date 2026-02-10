from xml.dom.minidom import ProcessingInstruction

import pandas as pd

data={
    "Name":["A","B","C","D"],
    "Marks":[90,91,92,93]
}

df=pd.DataFrame(data)
# print(df)

# print(df.head())
# print(df.info)
# print(df.describe())

# print(df["Name"])
# print(df["Marks"])
# print(df[["Name","Marks"]])

top=df[df["Marks"]>=92]
# print(top)

df["Grade"]=["C","B","A","A"]

print(df)
