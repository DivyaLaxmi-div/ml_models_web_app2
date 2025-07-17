import streamlit as st
import numpy as np
import pickle
from streamlit_option_menu import option_menu

# Load trained models
house_model = pickle.load(open('housepredict.sav', 'rb'))
loan_model = pickle.load(open('loanpredict.sav', 'rb'))

# Sidebar Menu
with st.sidebar:
    selected = option_menu(
        'ML Prediction Models',
        ['House Price Prediction', 'Loan Approval Prediction'],
        icons=['house-door', 'currency-rupee'],
        default_index=0
    )

# ------------------ HOUSE PRICE PREDICTION ------------------
if selected == 'House Price Prediction':
    st.title('🏠 California House Price Prediction')

    col1, col2 = st.columns(2)
    with col1:
        MedInc = st.number_input('Median Income (MedInc)', min_value=0.0)
        HouseAge = st.number_input('House Age', min_value=0.0)
        AveRooms = st.number_input('Average Number of Rooms (AveRooms)', min_value=0.0)
        AveBedrms = st.number_input('Average Number of Bedrooms (AveBedrms)', min_value=0.0)

    with col2:
        Population = st.number_input('Population', min_value=0.0)
        AveOccup = st.number_input('Average Occupants per Household (AveOccup)', min_value=0.0)
        Latitude = st.number_input('Latitude', min_value=-90.0, max_value=90.0)
        Longitude = st.number_input('Longitude', min_value=-180.0, max_value=180.0)

    if st.button("Predict House Price"):
        input_data = [MedInc, HouseAge, AveRooms, AveBedrms,
                      Population, AveOccup, Latitude, Longitude]

        input_np = np.array(input_data).reshape(1, -1)
        prediction = house_model.predict(input_np)
        st.success(f"🏡 Estimated House Price: ${prediction[0] * 100000:.2f}")


# ------------------ LOAN APPROVAL PREDICTION ------------------
elif selected == 'Loan Approval Prediction':
    st.title('💰 Loan Approval Prediction')

    col1, col2, col3 = st.columns(3)

    with col1:
        Gender = st.selectbox('Gender', ['Male', 'Female'])
        Married = st.selectbox('Married', ['Yes', 'No'])
        Dependents = st.selectbox('Dependents', ['0', '1', '2', '3+'])

    with col2:
        Education = st.selectbox('Education', ['Graduate', 'Not Graduate'])
        Self_Employed = st.selectbox('Self Employed', ['Yes', 'No'])
        ApplicantIncome = st.number_input('Applicant Income', min_value=0.0)
        CoapplicantIncome = st.number_input('Coapplicant Income', min_value=0.0)

    with col3:
        LoanAmount = st.number_input('Loan Amount (in thousands)', min_value=0.0)
        Loan_Amount_Term = st.number_input('Loan Term (in months)', min_value=0.0)
        Credit_History = st.selectbox('Credit History', [1.0, 0.0])
        Property_Area = st.selectbox('Property Area', ['Urban', 'Semiurban', 'Rural'])

    if st.button("Predict Loan Status"):
        # Convert categorical to numerical
        Gender = 1 if Gender == 'Male' else 0
        Married = 1 if Married == 'Yes' else 0
        Education = 1 if Education == 'Graduate' else 0
        Self_Employed = 1 if Self_Employed == 'Yes' else 0
        Dependents = 3 if Dependents == '3+' else int(Dependents)
        Property_Area = {'Urban': 2, 'Semiurban': 1, 'Rural': 0}[Property_Area]

        input_data = [Gender, Married, Dependents, Education, Self_Employed,
                      ApplicantIncome, CoapplicantIncome, LoanAmount,
                      Loan_Amount_Term, Credit_History, Property_Area]

        input_np = np.array(input_data).reshape(1, -1)
        result = loan_model.predict(input_np)

        if result[0] == 1:
            st.success("✅ Loan Approved")
        else:
            st.error("❌ Loan Not Approved")
