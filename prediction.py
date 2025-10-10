import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np
import io
from google.colab import files

# --- UPLOAD FILES (You must upload both 'goated' and 'ratings.csv') ---
uploaded = files.upload()

# --- STEP 1: LOAD DATA AND ROBUSTLY CLEAN COLUMN NAMES ---

# Safely find the uploaded filenames.
goated_file_key = [k for k in uploaded.keys() if 'goated' in k][0]
ratings_file_key = [k for k in uploaded.keys() if 'ratings.csv' in k][0]

# 1. Load the Segmented (GOATED) Data
df_segmented = pd.read_csv(io.BytesIO(uploaded[goated_file_key]), sep=';')

# 2. Load the Original Ratings Data
df_ratings = pd.read_csv(io.BytesIO(uploaded[ratings_file_key]))


# --- CRITICAL FIX: Clean all column names from RapidMiner output ---
# This removes all quotes and leads to the intended simple names
new_cols = {}
for col in df_segmented.columns:
    # Strip leading/trailing quotes, spaces, and replace complex names with simple ones
    clean_col = col.strip().replace('"', '').replace('average(rating)', 'Average_Rating_ZScore').replace('countWithOutMissings(movieId)', 'Total_Movies_Rated_ZScore').replace('standard_deviation(rating)', 'StdDev_Rating_ZScore').replace('cluster', 'Cluster_ID').replace('userId', 'userId')
    new_cols[col] = clean_col

df_segmented.rename(columns=new_cols, inplace=True)

# Final type conversion and quote removal
df_segmented['userId'] = df_segmented['userId'].astype(int)
df_segmented['Cluster_ID'] = df_segmented['Cluster_ID'].astype(str).str.strip()


print(f"Segmented Data Loaded from: {goated_file_key}. Column names successfully cleaned.")

# ----------------------------------------------------------------------
## --- STEP 2: CREATE PREDICTION LABEL ---

# 1. Calculate the RAW total number of ratings per user
df_raw_counts = df_ratings.groupby('userId')['movieId'].count().reset_index()
df_raw_counts.columns = ['userId', 'Raw_Rating_Count']

# 2. Merge the raw count back into the segmented data
df_final = pd.merge(df_segmented, df_raw_counts, on='userId', how='inner')

# 3. Define the prediction target: High Activity (> 50 ratings) vs. Low Activity
HIGH_ACTIVITY_THRESHOLD = 50
df_final['Activity_Level'] = np.where(
    df_final['Raw_Rating_Count'] > HIGH_ACTIVITY_THRESHOLD, 'High', 'Low'
)

# ----------------------------------------------------------------------
## --- STEP 3: TRAIN PREDICTION MODEL (Decision Tree) ---

# Features are the Z-scores: Avg Rating and StdDev Rating
X = df_final[['Average_Rating_ZScore', 'StdDev_Rating_ZScore']]
y = df_final['Activity_Level']

# Split data (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Train the Decision Tree Classifier
dt_classifier = DecisionTreeClassifier(max_depth=5, random_state=42)
dt_classifier.fit(X_train, y_train)

# Evaluate
y_pred = dt_classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print("\n--- Prediction Model Results ---")
print(f"Decision Tree Model Accuracy: {accuracy:.4f}")

# ----------------------------------------------------------------------
## --- STEP 4: EXPORT FOR POWER BI ---

# EXPORT 1: Segmented Users Data
df_export_segments = df_final[[
    'userId',
    'Cluster_ID',
    'Total_Movies_Rated_ZScore',
    'Average_Rating_ZScore',
    'StdDev_Rating_ZScore',
    'Activity_Level'
]]
df_export_segments.to_csv('1_Segmented_Users_for_PowerBI.csv', index=False)

# EXPORT 2: Model Performance Metrics
df_export_metrics = pd.DataFrame({
    'Metric': ['Accuracy', 'True Negative (Low)', 'False Positive', 'False Negative', 'True Positive (High)'],
    'Value': [accuracy, conf_matrix[0, 0], conf_matrix[0, 1], conf_matrix[1, 0], conf_matrix[1, 1]]
})
df_export_metrics.to_csv('2_Prediction_Metrics_for_PowerBI.csv', index=False)

# Download files
files.download('1_Segmented_Users_for_PowerBI.csv')
files.download('2_Prediction_Metrics_for_PowerBI.csv')

print("\nFinal CSV files prepared for Power BI and downloaded.")
