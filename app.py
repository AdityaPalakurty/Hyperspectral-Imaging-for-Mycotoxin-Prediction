import streamlit as st
import pandas as pd
from scripts.preprocess import preprocess_data
from scripts.inference import predict
import sys
import os

sys.path.append(os.path.abspath("scripts"))
st.set_page_config(page_title="Hyperspectral Imaging Mycotoxin Prediction", layout="wide")
st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <h1>Hyperspectral Imaging Mycotoxin Prediction</h1>
        <span style="font-size: 20px; font-weight: bold; color: cyan;">Aditya</span>
    </div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📂 Uploaded Data")
    st.dataframe(df.head()) 

    X_pca = preprocess_data(df)
    predictions = predict(X_pca)

    prediction_df = df.copy()
    prediction_df["Predicted vomitoxin_ppb"] = predictions

    st.subheader("🔮 Predicted Values")
    st.dataframe(prediction_df[["Predicted vomitoxin_ppb"]]) 

    st.download_button(
        "⬇️ Download Predictions",
        prediction_df.to_csv(index=False),
        file_name="predictions.csv",
        mime="text/csv"
    )
