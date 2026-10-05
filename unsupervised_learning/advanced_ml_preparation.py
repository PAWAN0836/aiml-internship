import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


# ==============================
# 1. Student Dataset
# ==============================

data = {
    "Study_Hours": [
        2, 3, 4, 5, 6,
        7, 8, 2, 3, 4,
        5, 6, 7, 8, 9,
        1, 3, 5, 7, 9
    ],

    "Attendance": [
        60, 65, 70, 75, 80,
        85, 90, 55, 62, 68,
        74, 82, 88, 92, 95,
        50, 64, 76, 86, 94
    ],

    "Assignment_Score": [
        45, 50, 55, 60, 65,
        70, 80, 40, 48, 54,
        62, 68, 75, 85, 90,
        35, 52, 64, 78, 88
    ],

    "Previous_Marks": [
        40, 45, 50, 55, 60,
        65, 75, 35, 42, 48,
        58, 64, 70, 80, 85,
        30, 46, 60, 72, 82
    ]
}


df = pd.DataFrame(data)


# ==============================
# 2. Feature Engineering
# ==============================

df["Average_Score"] = (
    df["Assignment_Score"] + df["Previous_Marks"]
) / 2

df["Study_Attendance_Index"] = (
    df["Study_Hours"] * df["Attendance"]
) / 100


print("===== DATA AFTER FEATURE ENGINEERING =====")
print(df)


# ==============================
# 3. Select Features
# ==============================

features = [
    "Study_Hours",
    "Attendance",
    "Assignment_Score",
    "Previous_Marks",
    "Average_Score",
    "Study_Attendance_Index"
]

X = df[features]


# ==============================
# 4. Feature Scaling
# ==============================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print("\n===== SCALED FEATURES =====")
print(X_scaled)


# ==============================
# 5. K-Means Clustering
# ==============================

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(X_scaled)


print("\n===== CLUSTERED DATA =====")
print(df)


# ==============================
# 6. Silhouette Score
# ==============================

silhouette = silhouette_score(
    X_scaled,
    df["Cluster"]
)

print("\nSilhouette Score:", silhouette)


# ==============================
# 7. Find Best K
# ==============================

results = []

for k in range(2, 6):

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(X_scaled)

    score = silhouette_score(
        X_scaled,
        labels
    )

    results.append([k, score])


results_df = pd.DataFrame(
    results,
    columns=["K", "Silhouette_Score"]
)


print("\n===== K VALUE COMPARISON =====")
print(results_df)


# ==============================
# 8. Best K
# ==============================

best_k = results_df.loc[
    results_df["Silhouette_Score"].idxmax(),
    "K"
]

best_score = results_df["Silhouette_Score"].max()


print("\nBest K:", best_k)
print("Best Silhouette Score:", best_score)


# ==============================
# 9. Final K-Means Model
# ==============================

final_model = KMeans(
    n_clusters=int(best_k),
    random_state=42,
    n_init=10
)

df["Final_Cluster"] = final_model.fit_predict(X_scaled)


# ==============================
# 10. Cluster Summary
# ==============================

cluster_summary = df.groupby("Final_Cluster")[
    [
        "Study_Hours",
        "Attendance",
        "Assignment_Score",
        "Previous_Marks",
        "Average_Score"
    ]
].mean()


print("\n===== CLUSTER SUMMARY =====")
print(cluster_summary)