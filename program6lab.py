import pandas as pd
import matplotlib.pyplot as plt
print("STEP 1 DATA SELECTION")
data ={
"Name":  ["Asha", "Rahul", "Priya", "Kiran", "Sneha"],
"Maths":  [85, 40, 78, 92, 551],
"Science":  [190, 45, 80, 95, 601],
"English":  [88, 50, 82, 91, 58]
}
df= pd.DataFrame (data)
print (df)
print ("\nSTEP 2 :DATA CLEANING")
df= df.drop_duplicates ()
print (df)
print("\nSTEP 3: DATA TRANSFORMATION")
df ["Average"] =(df ["Maths"] + df ["Science"] + df ["English"]) / 3
print(df)
print("\nSTEP 4: DATA MINING")
top_students = df[df ["Average"] > 75 ]
print("Top Performing students")
print(df)        
print (top_students [["Name", "Average"]])
print("\nSTEP 5: PATTERN EVALUATION")
print("Number of Top students:", len (top_students))
print("\nSTEP 6 KNOWLEDGE PRESENTATION")
plt.figure(figsize=(8,5))
plt.plot(df ["Name"],
df ["Average"], marker='o',
linewidth=2)
plt.title("student Average Marks")
plt.xlabel("students")
plt.ylabel("Average Marks")
plt.grid(True)
plt.show()
