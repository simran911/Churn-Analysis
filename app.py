import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained model
model_path = 'model.sav'
model = pickle.load(open(model_path, 'rb'))

df = pd.read_csv("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")
st.title("Customer Churn Prediction")

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox('Gender', df['gender'].unique())
    gender = 1 if gender == 'Male' else 0

with col2:
    SeniorCitizen = st.selectbox('Senior Citizen', df['SeniorCitizen'].unique())
    SeniorCitizen = 1 if SeniorCitizen == 1 else 0

with col3:
    Partner = st.selectbox('Married', df['Partner'].unique())
    Partner = 1 if Partner == 'Yes' else 0

with col1:
    Dependents = st.selectbox('Dependents', df['Dependents'].unique())
    Dependents = 1 if Dependents == 'Yes' else 0

with col2:
    tenure = st.number_input("Enter some tenure:")

with col3:
    PhoneService = st.selectbox('PhoneService', df['PhoneService'].unique())
    PhoneService = 1 if PhoneService == 'Yes' else 0

with col1:
    MultipleLines = st.selectbox('MultipleLines', df['MultipleLines'].unique())
    if MultipleLines == 'No phone service':
        MultipleLines = 0
    elif MultipleLines == 'No':
        MultipleLines = 1
    else:
        MultipleLines = 2

with col2:
    InternetService = st.selectbox('InternetService', df['InternetService'].unique())
    if InternetService == 'DSL':
        InternetService = 0
    elif InternetService == 'Fiber optic':
        InternetService = 1
    else:
        InternetService = 2

with col3:
    OnlineSecurity = st.selectbox('OnlineSecurity ', df['OnlineSecurity'].unique())
    if OnlineSecurity == 'No':
        OnlineSecurity = 0
    elif OnlineSecurity == 'Yes':
        OnlineSecurity = 1
    else:
        OnlineSecurity = 2

with col1:
    OnlineBackup = st.selectbox('OnlineBackup ', df['OnlineBackup'].unique())
    if OnlineBackup == 'No internet service':
        OnlineBackup = 0
    elif OnlineBackup == 'No':
        OnlineBackup = 1
    else:
        OnlineBackup = 2

with col2:
    DeviceProtection = st.selectbox('DeviceProtection ', df['DeviceProtection'].unique())
    if DeviceProtection == 'No internet service':
        DeviceProtection = 0
    elif DeviceProtection == 'No':
        DeviceProtection = 1
    else:
        DeviceProtection = 2

with col3:
    TechSupport = st.selectbox('TechSupport ', df['TechSupport'].unique())
    if TechSupport == 'No internet service':
        TechSupport = 0
    elif TechSupport == 'No':
        TechSupport = 1
    else:
        TechSupport = 2

with col1:
    StreamingTV = st.selectbox('StreamingTV', df['StreamingTV'].unique())
    if StreamingTV == 'No internet service':
        StreamingTV = 0
    elif StreamingTV == 'No':
        StreamingTV = 1
    else:
        StreamingTV = 2

with col2:
    StreamingMovies = st.selectbox('StreamingMovies', df['StreamingMovies'].unique())
    if StreamingMovies == 'No internet service':
        StreamingMovies = 0
    elif StreamingMovies == 'No':
        StreamingMovies = 1
    else:
        StreamingMovies = 2

with col3:
    Contract = st.selectbox('Contract ', df['Contract'].unique())
    if Contract == 'Month-to-month':
        Contract = 0
    elif Contract == 'One year':
        Contract = 1
    else:
        Contract = 2

with col1:
    PaperlessBilling = st.selectbox('PaperlessBilling', df['PaperlessBilling'].unique())
    PaperlessBilling = 1 if PaperlessBilling == 'Yes' else 0

with col2:
    PaymentMethod = st.selectbox('PaymentMethod', df['PaymentMethod'].unique())
    if PaymentMethod == 'Bank transfer (automatic)':
        PaymentMethod = 0
    elif PaymentMethod == 'Credit card (automatic)':
        PaymentMethod = 1
    elif PaymentMethod == 'Electronic check':
        PaymentMethod = 2
    else:
        PaymentMethod = 3

with col3:
    MonthlyCharges = st.number_input("Enter your monthly charges:")

# code for Prediction
churn_prediction = None  # Initialize the variable

if st.button('Predict churn'):
    user_input = [[gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService,
                   MultipleLines, InternetService, OnlineSecurity, OnlineBackup,
                   DeviceProtection, TechSupport, StreamingTV, StreamingMovies,
                   Contract, PaperlessBilling, PaymentMethod, MonthlyCharges]]

    churn_prediction = model.predict(user_input)

if churn_prediction is not None:
    if churn_prediction[0] == 1:
        st.write("The customer will leave the bank")
    else:
        st.write("The customer will not leave the bank")
