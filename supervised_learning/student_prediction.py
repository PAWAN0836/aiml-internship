import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import (
    mean_absolute_error,
    r2_score,
    accuracy_score
)


# Dataset
data = {
    "Study_Hours": [
        2, 3, 4, 5, 6,
        7, 8, 1, 3, 5,
        6, 7, 2, 4, 8,
        9, 1, 2, 6, 7
    ],

    "Attendance": [
        60, 65, 70, 75, 80,
        85, 90, 55, 68, 78,
        82, 88, 62, 72, 95,
        92, 50, 58, 84, 89
    ],

    "Assignment_Score": [
        40, 45, 50, 55, 60,
        65, 70, 35, 48, 58,
        62, 68, 42, 52, 75,
        78, 30, 38, 64, 70
    ],

    "Previous_Marks": [
        45, 50, 55, 60, 65,
        70, 75, 40, 52, 62,
        68, 72, 48, 58, 80,
        82, 35, 43, 67, 74
    ],

    "Final_Marks": [
        48, 52, 58, 63, 68,
        73, 78, 42, 55, 65,
        70, 75, 50, 60, 83,
        85, 38, 46, 69, 77
    ]
}


df = pd.DataFrame(data)


# Create Pass/Fail target
df["Result"] = df["Final_Marks"].apply(
    lambda marks: 1 if marks >= 40 else 0
)


print("===== STUDENT DATASET =====")
print(df)


# Features
features = [
    "Study_Hours",
    "Attendance",
    "Assignment_Score",
    "Previous_Marks"
]

X = df[features]


# ==============================
# REGRESSION
# ==============================

y_marks = df["Final_Marks"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_marks,
    test_size=0.2,
    random_state=42
)


regression_model = LinearRegression()

regression_model.fit(X_train, y_train)

marks_prediction = regression_model.predict(X_test)


mae = mean_absolute_error(
    y_test,
    marks_prediction
)

r2 = r2_score(
    y_test,
    marks_prediction
)


print("\n===== REGRESSION =====")

print("Actual Marks:")
print(list(y_test))

print("\nPredicted Marks:")
print([round(x, 2) for x in marks_prediction])

print("\nMean Absolute Error:", round(mae, 2))
print("R2 Score:", round(r2, 2))


# ==============================
# CLASSIFICATION
# ==============================

y_result = df["Result"]


X_train_c, X_test_c, y_train_c, y_test_c = train_test_split(
    X,
    y_result,
    test_size=0.2,
    random_state=42
)


classification_model = LogisticRegression(
    max_iter=1000
)

classification_model.fit(
    X_train_c,
    y_train_c
)


result_prediction = classification_model.predict(X_test_c)


accuracy = accuracy_score(
    y_test_c,
    result_prediction
)


print("\n===== CLASSIFICATION =====")

print("Actual Results:")
print(
    ["Pass" if x == 1 else "Fail" for x in y_test_c]
)

print("\nPredicted Results:")
print(
    ["Pass" if x == 1 else "Fail" for x in result_prediction]
)

print(
    "\nClassification Accuracy:",
    round(accuracy * 100, 2),
    "%"
)


# ==============================
# NEW STUDENT
# ==============================

new_student = pd.DataFrame({
    "Study_Hours": [6],
    "Attendance": [85],
    "Assignment_Score": [65],
    "Previous_Marks": [70]
})


predicted_marks = regression_model.predict(
    new_student
)[0]

predicted_result = classification_model.predict(
    new_student
)[0]


print("\n===== NEW STUDENT =====")

print("Predicted Final Marks:",
      round(predicted_marks, 2))


if predicted_result == 1:
    print("Predicted Result: PASS")
else:
    print("Predicted Result: FAIL")