from sklearn.linear_model import LinearRegression

X = [[1],[2],[3],[4],[5]] #model always expects 2D
y = [50,60,70,80,90]

model=LinearRegression()
model.fit(X,y)

print(model.predict([[6]]))