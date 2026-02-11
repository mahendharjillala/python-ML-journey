import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_csv("house_data.csv")

X = df[["size"]]
y = df["price"]

model = LinearRegression()
model.fit(X, y)


joblib.dump(model,"house_price_model.pkl")
