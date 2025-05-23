# -*- coding: utf-8 -*-
"""Streamlit file.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1k-9owPNABviq5woafn0g9vDqjSQahiI3
"""

import streamlit as st
import numpy as np
import pickle
import tensorflow as tf
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


# Load the trained model
from tensorflow.keras.models import load_model

model = load_model('churn_model.h5')


# Load the scaler
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

st.title("📊 Customer Churn Prediction - ANN Model")

# 🎛️ Hyperparameter Selection
epochs = st.slider("🔄 Select Epochs", min_value=10, max_value=100, value=50, step=10)
batch_size = st.radio("📦 Select Batch Size", [16, 32, 64], index=1)
activation = st.selectbox("⚡ Select Activation Function", ["relu", "sigmoid", "tanh"])
optimizer = st.selectbox("🚀 Select Optimizer", ["adam", "sgd", "rmsprop"])

# 📊 Input Fields
tenure = st.number_input("📅 Tenure (months)", min_value=0, max_value=72, value=12)
monthly_charges = st.number_input("💵 Monthly Charges", min_value=0.0, max_value=200.0, value=50.0)
total_charges = st.number_input("💰 Total Charges", min_value=0.0, max_value=10000.0, value=500.0)
contract = st.selectbox("📑 Contract Type", ["Month-to-Month", "One Year", "Two Year"])

# Convert categorical values (one-hot encoding for contract type)
contract_map = {"Month-to-Month": [1, 0, 0], "One Year": [0, 1, 0], "Two Year": [0, 0, 1]}
contract_value = contract_map[contract]

# Prepare input data with the correct number of features the scaler was trained on
# Assuming the scaler was trained on the 3 numerical features + 7 other features (total 10)
input_data = np.array([[tenure, monthly_charges, total_charges] + [0]*7])  # Adjust the number of zeros as needed

# Apply one-hot encoding to contract value if necessary (depends on how the model was trained)
# input_data = np.concatenate([input_data, contract_value], axis=1) #Concatenate one-hot encoded contract value to input_data.

input_data = scaler.transform(input_data)  # Scale input


# 🏆 Prediction Button
if st.button("🔍 Predict Churn"):
    prediction = model.predict(input_data)[0][0]
    if prediction > 0.5:
        st.error(f"⚠️ High chance of churn (Score: {prediction:.2f})")
    else:
        st.success(f"✅ Customer likely to stay (Score: {prediction:.2f})")

# 📈 Graphs Section
st.subheader("📊 Model Performance")

# Placeholder for accuracy & loss graph
loss_fig, loss_ax = plt.subplots()
loss_ax.plot([0.6, 0.4, 0.3], label="Training Loss")
loss_ax.plot([0.7, 0.5, 0.35], label="Testing Loss")
loss_ax.set_xlabel("Epochs")
loss_ax.set_ylabel("Loss")
loss_ax.legend()
st.pyplot(loss_fig)

accuracy_fig, accuracy_ax = plt.subplots()
accuracy_ax.plot([0.75, 0.80, 0.85], label="Training Accuracy")
accuracy_ax.plot([0.72, 0.78, 0.83], label="Testing Accuracy")
accuracy_ax.set_xlabel("Epochs")
accuracy_ax.set_ylabel("Accuracy")
accuracy_ax.legend()
st.pyplot(accuracy_fig)

st.write("✅ Model is trained with the selected hyperparameters. You can re-run the model with different settings!")

# Plot Accuracy & Loss
st.subheader("📈 Training Results")

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load dataset
url = "https://raw.githubusercontent.com/055058vandana/ANN_Project/refs/heads/main/anndataset.csv"
df = pd.read_csv(url)

# Define train data and labels
feature_cols = ['tenure', 'MonthlyCharges', 'TotalCharges', 'SeniorCitizen',
                'Contract', 'PaymentMethod', 'InternetService', 'OnlineSecurity',
                'TechSupport', 'PaperlessBilling']

target_col = 'Churn'

# Encode categorical variables
label_encoders = {}
for col in df.select_dtypes(include=['object']).columns:
    if col != 'customerID':
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

# Define train data and labels
train_data = df[feature_cols]
train_labels = df[target_col]

# Split data into training and validation sets
train_data, val_data, train_labels, val_labels = train_test_split(train_data, train_labels, test_size=0.2, random_state=42)

# Scale features
scaler = StandardScaler()
train_data = scaler.fit_transform(train_data)
val_data = scaler.transform(val_data)

print("Train data and labels are defined successfully.")

# Train the model and store history
history = model.fit(train_data, train_labels, 
                    validation_data=(val_data, val_labels), 
                    epochs=epochs, batch_size=batch_size)


# Plot Accuracy
ax[0].plot(history.history["accuracy"], label="Train Accuracy")
ax[0].plot(history.history["val_accuracy"], label="Test Accuracy")
ax[0].set_title("Model Accuracy")
ax[0].set_xlabel("Epochs")
ax[0].set_ylabel("Accuracy")
ax[0].legend()

# Plot Loss
ax[1].plot(history.history["loss"], label="Train Loss")
ax[1].plot(history.history["val_loss"], label="Test Loss")
ax[1].set_title("Model Loss")
ax[1].set_xlabel("Epochs")
ax[1].set_ylabel("Loss")
ax[1].legend()

# Show the plot in Streamlit
st.pyplot(fig)

# Save the trained model
with open("churn.pkl", "wb") as f:
    pickle.dump(model, f)

# Assuming you also have a scaler, save that as well (if needed)
with open("scaler.pkl", "wb") as f:
    pickle.dump(scaler, f)

st.success("✅ Model training complete! `churn.pkl` & `scaler.pkl` saved.")

with open("app.py", "w") as f:
    f.write("""
import streamlit as st
import numpy as np
import tensorflow as tf
import pickle

# Load the trained model
model = tf.keras.models.load_model('churn_model.h5')

# Load the scaler
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

st.title("Customer Churn Prediction")

# Input fields for user
tenure = st.number_input("Tenure (months)", min_value=0, max_value=72, value=12)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, max_value=200.0, value=50.0)
total_charges = st.number_input("Total Charges", min_value=0.0, max_value=10000.0, value=500.0)
contract = st.selectbox("Contract Type", ["Month-to-Month", "One Year", "Two Year"])

# Convert categorical values
contract_map = {"Month-to-Month": 0, "One Year": 1, "Two Year": 2}
contract_value = contract_map[contract]

# Prepare input data
input_data = np.array([[tenure, monthly_charges, total_charges, contract_value]])
input_data = scaler.transform(input_data)  # Scale input

# Predict button
if st.button("Predict Churn"):
    prediction = model.predict(input_data)[0][0]
    if prediction > 0.5:
        st.error(f"High chance of churn (Score: {prediction:.2f})")
    else:
        st.success(f"Customer likely to stay (Score: {prediction:.2f})")
""")
