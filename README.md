# 🧠 ML Web App – House Price & Loan Approval Prediction

This project is a **Machine Learning-powered Streamlit Web Application** that provides predictions using two models:

- ✅ **Regression Model** – Predicts California House Prices  
- ✅ **Classification Model** – Predicts Loan Approval Status  

The app is deployed using **Streamlit Cloud**, and provides a simple, interactive UI for users to input data and receive predictions.

---

## 🔍 Models Overview

### 1. 🏠 California House Price Prediction (Regression)

- **Model Type**: Regression  
- **Dataset**: California Housing Dataset *(not Boston)*  
- **Target Variable**: Median House Value  
- **Algorithm Used**: XGBoost Regressor  
- **Features**:
  - `MedInc` – Median Income
  - `HouseAge` – House Age
  - `AveRooms` – Average Number of Rooms
  - `AveBedrms` – Average Number of Bedrooms
  - `Population` – Population in the block
  - `AveOccup` – Average Household Occupancy
  - `Latitude` – Latitude coordinate
  - `Longitude` – Longitude coordinate

📌 This model predicts the **estimated house price** based on input housing characteristics using California housing data.

---

### 2. 💰 Loan Approval Prediction (Classification)

- **Model Type**: Classification  
- **Dataset**: Loan Prediction Dataset  
- **Target Variable**: Loan Status (Approved or Not Approved)  
- **Algorithm Used**: XGBoost Classifier  
- **Features**:
  - `Gender`, `Married`, `Dependents`
  - `Education`, `Self_Employed`
  - `ApplicantIncome`, `CoapplicantIncome`
  - `LoanAmount`, `Loan_Amount_Term`
  - `Credit_History`, `Property_Area`

📌 This model predicts whether a loan **application will be approved** based on applicant information.

---

## ⚙️ How It Works

1. Models are trained and saved as `.sav` files using `pickle`.
2. The Streamlit app loads these models and provides a UI for predictions.
3. `streamlit-option-menu` is used for tab-like navigation between models.
4. All numerical and categorical inputs are handled properly with conversions.

---
## 🔗 Live Demo

Click the link below to access the deployed ML Models Web App:

👉 [Open App on Streamlit](https://mlmodelswebapp2-sk4tntsrva88mbukrdpgqx.streamlit.app/)


## 📦 Dependencies

All required packages are listed in `requirements.txt`.  
Make sure the following are installed:

```txt
streamlit
numpy
pickle
scikit-learn
xgboost
streamlit-option-menu


