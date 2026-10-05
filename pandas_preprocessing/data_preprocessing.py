
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO


# Sample dataset
data = """Name,Age,Marks,Attendance,Result
Rahul,20,80,90,Pass
Priya,21,75,85,Pass
Aman,20,,88,Pass
Sneha,22,65,70,Pass
Rahul,20,80,90,Pass
Ravi,21,45,60,Fail
"""


# Load dataset
df = pd.read_csv(StringIO(data))

print("===== ORIGINAL DATA =====")
print(df)


# Check missing values
print("\n===== MISSING VALUES =====")
print(df.isnull().sum())


# Fill missing marks with mean
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())


# Remove duplicates
df = df.drop_duplicates()


# Select features
features = df[["Age", "Marks", "Attendance"]]

# Select target
target = df["Result"]


print("\n===== PROCESSED DATA =====")
print(df)

print("\n===== FEATURES =====")
print(features)

print("\n===== TARGET =====")
print(target)


# Visualization
plt.bar(df["Name"], df["Marks"])

plt.xlabel("Student")
plt.ylabel("Marks")
plt.title("Student Marks")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()