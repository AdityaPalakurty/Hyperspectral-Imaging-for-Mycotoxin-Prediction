import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA

def load_scalers():
    with open("models/scaler.pkl", "rb") as f:
        scaler = pickle.load(f)
    with open("models/pca.pkl", "rb") as f:
        pca = pickle.load(f)
    return scaler, pca

def preprocess_data(df):
    scaler, pca = load_scalers()
    X = df.iloc[:, 1:].values
    X_scaled = scaler.transform(X)
    X_pca = pca.transform(X_scaled)
    return X_pca