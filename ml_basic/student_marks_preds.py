import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split



data = {
    "Hours": [1,2,3,4,5,6,7,8,9,10],
    "Marks": [45,50,55,65,70,78,82,88,92,95]
}

df=pd.DataFrame(data)

X=df[["Hours"]]
y=df["Marks"]

X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.2,random_state=42
)

model=LinearRegression()
model.fit(X_train,y_train)

hrs=int(input("enter hrs:"))
input_df = pd.DataFrame([[hrs]], columns=["Hours"])
preds=model.predict(input_df)
print("Predict:", preds)

plt.scatter(X_train, y_train, label="Training Data")
plt.scatter(X_test, y_test, label="Actual Test Data")

plt.plot(X, model.predict(X), label="Regression Line")


plt.legend()
plt.show()