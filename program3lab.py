import pandas as pd print("STEP 1: DATA SELECTION")
data (
"Name": ["Anil", "Bharath", "Charan", "Deepa", "Farah"], "Age": [24, 26, 25, 28, 27], "Salary": [35000, 42000, None, 50000, 48000]
df pd. DataFrame (data)
print (df) print("\nSTEP 2: DATA PREPROCESSING")
average_salary df ["Salary"].mean ()
df ["Salary"] df("Salary"].fillna (average_salary)
print (df)
print("\nSTEP 3: DATA TRANSFORMATION")
print(df) print("\nSTEP 4 FINAL DATASET")
print(df)



