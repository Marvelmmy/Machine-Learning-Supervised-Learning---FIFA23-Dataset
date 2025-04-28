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
