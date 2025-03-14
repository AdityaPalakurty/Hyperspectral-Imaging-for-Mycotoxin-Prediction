# Hyperspectral-Imaging-for-Mycotoxin-Prediction

This repository contains a **Streamlit-based web application** for predicting Deoxynivalenol (DON) concentration in Food samples using a neural network model.
The main objective is to process hyperspectral imaging data, perform dimensionality reduction, and develop a machine learning model to predict mycotoxin levels in corn samples.

## 📂 Repository Structure
```
DON-Prediction/
├── models/             # Trained models and scalers
│   ├── pca.pkl         # Saved PCA model
│   ├── scaler.pkl      # Feature MinMaxScaler
│   ├── y_scaler.pkl    # Target variable MinMaxScaler
│   ├── neural_net.h5   # Trained Neural Network model
│
├── scripts/            # Core scripts
│   ├── preprocess.py   # Data preprocessing (scaling, PCA)
│   ├── train.py        # Model training
│   ├── predict.py      # Model inference
│
├── app.py              # Streamlit web application
├── requirements.txt    # Required Python packages
├── README.md           # Documentation
```

## 🚀 Installation & Setup
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/DON-Prediction.git
   cd DON-Prediction
   ```
2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🛠 Usage
### 1️⃣ Preprocess Data
Run the preprocessing script to scale and apply PCA:
```bash
python scripts/preprocess.py
```

### 2️⃣ Train the Model
Train the neural network model:
```bash
python scripts/train.py
```

### 3️⃣ Make Predictions
Run the prediction script:
```bash
python scripts/predict.py
```

### 4️⃣ Run Streamlit App
Launch the Streamlit web app:
```bash
streamlit run app.py
```

## 📊 Model Details
- **Scaling:** MinMaxScaler was used for both features and target variable.
- **Dimensionality Reduction:** PCA was applied, selecting **4 components** to retain 95% variance.
- **Neural Network:** A sequential model with 3 hidden layers (128, 64, 32 neurons) and ReLU activations.

## 📌 Features
- Upload CSV file for batch predictions.
- Download prediction results.
