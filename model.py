#importing libraries 
import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, f1_score
from sklearn.preprocessing import StandardScaler

#define the targeted output (y >= 75)
df['Good'] = df['Overall'].apply(lambda x: if x >= 75 else 0)
#identifying the features
ml_features = df.drop(columns=['Good','Overall'])
ml_labels = df['Good']
X = ml_features.select_dtypes(include=['number'])
y = ml_labels
X_train, y_train, X_test, y_test =  train_test_split(X, y, test_size=0.2, random_state=46)
# Scale the features (if needed, optional)
scaler = StandardScaler()
scaler.fit(X_train)
X_train_scaled = scaler.transform(X_train)
# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=46)
model.fit(X_train_scaled, y_train)
# Make predictions using the test set
X_test_scaled = scaler.transform(X_test)
y_pred = model.predict(X_test_scaled)
# Evaluate the model
ml_accuracy = classification_report(y_test, y_pred)
ml_f1_score = f1_score(y_test, y_pred, average='macro')
print("Classification Report:\n", classification_report(y_test, y_pred))
print("F1 Score (macro):", f1_score(y_test, y_pred, average='macro'))
