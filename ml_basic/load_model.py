import joblib
model=joblib.load("house_price_model.pkl")


size = int(input("Enter house size: "))
print("Predicted price:", model.predict([[size]])[0])