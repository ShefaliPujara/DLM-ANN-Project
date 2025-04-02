# Artificial Neural Network (ANN) Model Deployment using Streamlit

## Project Overview
This project focuses on building and deploying an Artificial Neural Network (ANN) model using Streamlit. The model is trained to predict customer churn based on various factors such as demographics, account details, and service usage.

## Objectives
- Develop an ANN model to classify customer churn.
- Preprocess and analyze customer data.
- Deploy an interactive dashboard using Streamlit.
- Allow users to input new customer data and receive real-time predictions.

---
## Dashboard Link
[ANN Churn Prediction Dashboard](https://annproject-xrv9eb3ccwjrsqx4zc5tcs.streamlit.app/)

## Dataset Overview
### Data Source
The dataset used is `anndataset.csv`, which contains customer information with multiple features.

### Features and Target Variable
**Independent Variables (Features):**
- `SeniorCitizen`, `tenure`, `MonthlyCharges`, `TotalCharges`
- `gender`, `Partner`, `Dependents`, `PhoneService`, `MultipleLines`
- `InternetService`, `OnlineSecurity`, `OnlineBackup`, `DeviceProtection`
- `TechSupport`, `StreamingTV`, `StreamingMovies`, `Contract`
- `PaperlessBilling`, `PaymentMethod`

**Dependent Variable (Target):**
- `Churn` (Binary: `1 = Yes`, `0 = No`)

## Methodology
### Data Preprocessing
- **Handling Missing Values:** Imputed missing values for numerical features.
- **Encoding Categorical Variables:** Applied Label Encoding to convert categorical variables into numerical form.
- **Feature Scaling:** Standardized numerical features using `StandardScaler`.
- **Train-Test Split:** Split data into training (80%) and validation (20%) sets.

### Model Architecture
- **Input Layer:** Accepts numerical features.
- **Hidden Layers:** Two fully connected layers with ReLU activation.
- **Output Layer:** Uses sigmoid activation for binary classification.

### Implementation
#### Technologies Used
- **Python Libraries:** `Pandas`, `NumPy`, `Scikit-learn`, `TensorFlow`, `Keras`, `Streamlit`
- **Development Environment:** `Jupyter Notebook`, `Anaconda`, `Streamlit Cloud`

#### Model Training
```python
model.add(Dense(19, input_shape=(19,), activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
```
- **Loss Function:** Binary Cross-Entropy
- **Optimizer:** Adam
- **Evaluation Metric:** Accuracy

## Deployment Using Streamlit
- Built an interactive dashboard allowing users to input values and receive churn predictions.
- Hosted the app on Streamlit Community Cloud.
- Used `requirements.txt` to manage dependencies.

## Results & Evaluation
- **Training Accuracy:** 92%
- **Validation Accuracy:** 88%

### Key Findings
- Customers with longer tenure and lower monthly charges are less likely to churn.
- Contract type and payment method significantly impact churn probability.
- Users with no tech support and online security have a higher chance of leaving.
- Monthly charges have a strong correlation with churn behavior.

## Insights & Observations
- High-risk customers are those who have month-to-month contracts and use paperless billing.
- Loyal customers generally have long-term contracts and low monthly fees.
- Providing better tech support and security features could reduce churn rates significantly.
- Introducing discounts or incentives for long-term contracts might improve customer retention.

## Deployment Guide
### Running Locally
```bash
streamlit run ann.py
```

### Deploying on Streamlit Cloud
1. Push code to GitHub.
2. Connect GitHub repo to Streamlit Cloud.
3. Select `ann.py` as the entry point and deploy.

## Conclusion & Future Scope
### Conclusion
- Successfully built and deployed an ANN-based churn prediction model.
- Streamlit provides an intuitive interface for real-time predictions.
- Key customer insights can be leveraged to reduce churn rates.

### Future Scope
- Enhance the model with additional feature engineering.
- Deploy the model as a web API for broader accessibility.
- Optimize model hyperparameters using Grid Search.
- Implement real-time customer retention strategies based on predictions.

## References
- [TensorFlow Documentation](https://www.tensorflow.org/)
- [Streamlit Guide](https://docs.streamlit.io/)
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
