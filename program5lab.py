from sklearn. tree  import  DecisionTreeClassifier
marks =[[35], [40], [50], [60], [75], [85], [95]]
result= ["Fail", "Pass", "Pass", "Pass", "Pass", "Pass", "Pass"]
model=DecisionTreeClassifier()
model.fit (marks, result)
prediction =model.predict([[30], [70],[45]])
print("Predicted Results", prediction [2])
