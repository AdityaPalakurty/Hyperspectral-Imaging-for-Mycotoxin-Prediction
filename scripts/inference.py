import pickle
import numpy as np
import tensorflow as tf
import joblib

def load_model():
    model = tf.keras.models.load_model(
        "models/neural_net.h5",
        compile=False  
    )
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])  
    y_scaler = joblib.load("models/y_scaler.pkl")
    return model, y_scaler

def predict(X_pca):
    model, y_scaler = load_model()
    y_pred = model.predict(X_pca)
    y_pred = y_scaler.inverse_transform(y_pred)
    return y_pred