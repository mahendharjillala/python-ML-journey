from fastapi import FastAPI
import joblib


app=FastAPI()


model=joblib.load("/Users/mahendharjillala/Desktop/PythonProject/python_overnight/ml_basic/house_price_model.pkl")

@app.get("/")
def home():
    return {"message":"House Price Prediction API"}

@app.get("/predict")
def predict(size: int):
    pre = model.predict([[size]])[0]
    return {"Predicted Price": pre}