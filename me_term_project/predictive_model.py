import numpy as np
import pickle
from pathlib import Path
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.model_selection import KFold
import sklearn.model_selection
import sys
sys.path.insert(0, '../')
from helper.classification_tools import label_matcher

# Load data
fc1_path = Path('../data/features/VGG16_fc1_features_std.pickle')
le_path = Path('../models/label_encoder.pickle')

with open(fc1_path, 'rb') as f:
    data = pickle.load(f)
with open(le_path, 'rb') as f:
    le = pickle.load(f)

files = data['filename']
fc1 = data['features']
labels = data['labels']
y_gt = le.transform(labels)

# Train initial model
n_pca = 35
pca = PCA(n_components=n_pca, whiten=True, svd_solver='full')
x = pca.fit_transform(fc1)
kmeans = KMeans(n_clusters=7, init='k-means++', n_init=500, random_state=42)
kmeans.fit(x)

# Cross-validation (simplified)
kfold = KFold(n_splits=5, shuffle=True, random_state=42)
for train_idx, test_idx in kfold.split(x):
    x_train, x_test = x[train_idx], x[test_idx]
    y_train, y_test = y_gt[train_idx], y_gt[test_idx]
    
    kmeans_split = KMeans(n_clusters=7, init='k-means++', n_init=100).fit(x_train)
    y_pred_train = label_matcher(kmeans_split.labels_, y_train)
    y_pred_test = label_matcher(kmeans_split.predict(x_test), y_test)
    
    train_acc = np.mean(y_pred_train == y_train)
    test_acc = np.mean(y_pred_test == y_test)
    print(f"Train Acc: {train_acc:.4f}, Test Acc: {test_acc:.4f}")