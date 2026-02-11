import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df=pd.read_csv("house_data.csv")

X = df[["size"]]
y = df["price"]

X_train,X_test,y_train,y_test=train_test_split(
    X,y,test_size=0.2,random_state=42
)

model=LinearRegression()
model.fit(X_train,y_train)

new_size = int(input("Enter house size: "))
print("Predicted price:", model.predict([[new_size]])[0])



