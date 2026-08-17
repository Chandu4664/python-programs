from sklearn.linear_model import LinearRegression
house_size =[[1200], [1500], [1800], [2100], [2400]]
price=[48, 60, 72, 84, 96]
model=LinearRegression()
model.fit (house_size, price)
predicted_price =model.predict([[2000]])
print("Predicted House Price", predicted_price[0], "Lakhs")

