import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

data={
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



preds=model.predict(X_test)


print("Actual:",list(y_test))
print("preds:",list(preds))

print("error:",mean_absolute_error(y_test,preds))

plt.scatter(X_test, y_test, label="Actual")
plt.scatter(X_test, preds, label="Predicted")
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.legend()
plt.show()



