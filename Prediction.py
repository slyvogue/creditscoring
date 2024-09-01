import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pickle
import streamlit as st
import pandas as pd
from PIL import Image

# Load the data and model
data = pickle.load(open('data_for_deploy.pkl', 'rb'))
loaded_model = pickle.load(open('model.pkl', 'rb'))

# Load the preprocessor
preprocessor = pickle.load(open('preprocessor.pkl', 'rb'))

# Define function to make credit score prediction
def make_credit_score_prediction(age, month, annual_income, monthly_inhand_salary, monthly_balance, total_emi_per_month,
                                 num_bank_accounts, num_credit_inquiries, credit_history_age, num_of_loan, 
                                 num_of_delayed_payment, payment_behaviour, credit_utilization_ratio, delay_from_due_date,
                                 changed_credit_limit, amount_invested_monthly, num_credit_card, outstanding_debt,
                                 interest_rate, age_group, delay_group, credit_mix, occupation, payment_of_min_amount):
    
    # Prepare input data for prediction
    input_data = {
        'Age': age,
        'Month': month,
        'Annual_Income': annual_income,
        'Monthly_Inhand_Salary': monthly_inhand_salary,
        'Monthly_Balance': monthly_balance,
        'Total_EMI_per_month': total_emi_per_month,
        'Num_Bank_Accounts': num_bank_accounts,
        'Num_Credit_Inquiries': num_credit_inquiries,
        'Credit_History_Age': credit_history_age,
        'Num_of_Loan': num_of_loan,
        'Num_of_Delayed_Payment': num_of_delayed_payment,
        'Payment_Behaviour': payment_behaviour,
        'Credit_Utilization_Ratio': credit_utilization_ratio,
        'Delay_from_due_date': delay_from_due_date,
        'Changed_Credit_Limit': changed_credit_limit,
        'Amount_invested_monthly': amount_invested_monthly,
        'Num_Credit_Card': num_credit_card,
        'Outstanding_Debt': outstanding_debt,
        'Interest_Rate': interest_rate,
        'Age_Group': age_group,
        'Delay_Group': delay_group,
        'Credit_Mix': credit_mix,
        'Occupation': occupation,
        'Payment_of_Min_Amount': payment_of_min_amount
    }

    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data])

    # Preprocess the input data
    df_preprocessed = preprocessor.transform(input_df)
    
    # Make prediction
    credit_score = loaded_model.predict(df_preprocessed)
    
    return f"The predicted credit score percentage is: {credit_score[0]:.2%}"

# Streamlit app layout for credit score prediction
def app():
    st.title("Credit Score Prediction App")
    st.header("Enhancing Predictive Accuracy and Reliability with Machine Learning")
    st.markdown("""
        Welcome to the Credit Score Prediction App! This app uses a machine learning model to predict credit scores based on user inputs.
        You can enter your details in the sidebar and get your predicted credit score.
    """)

    # Input fields for user details
    with st.form("user_input_form"):
        st.sidebar.header("User Input Features")
        age = st.sidebar.number_input('Age', min_value=18, max_value=100)
        month = st.sidebar.number_input('Month', min_value=1, max_value=12)
        annual_income = st.sidebar.number_input('Annual_Income', min_value=0.00, max_value=300000.00)
        monthly_inhand_salary = st.sidebar.slider('Monthly_Inhand_Salary', min_value=2000, max_value=20000)
        monthly_balance = st.sidebar.slider('Monthly Balance', min_value=500, max_value=20000)
        total_emi_per_month = st.sidebar.number_input('Total_EMI_per_month', min_value=0.00, max_value=5000.00)
        num_bank_accounts = st.sidebar.number_input('Num_Bank_Accounts', min_value=0, max_value=20)
        num_credit_inquiries = st.sidebar.slider('Num_Credit_Inquiries', min_value=0, max_value=20000)
        credit_history_age = st.sidebar.number_input('Credit_History_Age', min_value=0, max_value=500)
        num_of_loan = st.sidebar.slider('Num_of_Loan', min_value=0.00, max_value=12.0)
        num_of_delayed_payment = st.sidebar.slider('Num_of_Delayed_Payment', 0, 25, 14, 1)
        payment_behaviour = st.sidebar.slider('Payment_Behaviour', min_value=1, max_value=6)
        credit_utilization_ratio = st.sidebar.slider('Credit_Utilization_Ratio', min_value=0.00, max_value=100.00)
        delay_from_due_date = st.sidebar.number_input('Delay_from_due_date', min_value=0, max_value=20)
        changed_credit_limit = st.sidebar.slider('Changed_Credit_Limit', 0.5, 30.0, 9.40, 0.1)
        amount_invested_monthly = st.sidebar.number_input('Amount_invested_monthly', min_value=0, max_value=20)
        num_credit_card = st.sidebar.number_input('Num_Credit_Card', min_value=0, max_value=12)
        outstanding_debt = st.sidebar.slider('Outstanding_Debt', 0.0, 5000.0, 1426.0, 0.1)
        interest_rate = st.sidebar.slider('Interest_Rate', 1, 34, 14, 1)
        age_group = st.sidebar.slider('Age_Group', min_value=1, max_value=4)
        delay_group = st.sidebar.slider('Delay_Group', min_value=1, max_value=4)
        credit_mix = st.sidebar.slider('Credit Mix', min_value=0, max_value=2)
        occupation = st.sidebar.number_input('Occupation', min_value=1, max_value=15)
        payment_of_min_amount = st.sidebar.number_input('Payment_of_Min_Amount', min_value=0, max_value=2)
        submit_button = st.form_submit_button("Make Prediction")

    # Button to make prediction
    if submit_button:
        prediction_result = make_credit_score_prediction(age, month, annual_income, monthly_inhand_salary, monthly_balance,
                                                         total_emi_per_month, num_bank_accounts, num_credit_inquiries,
                                                         credit_history_age, num_of_loan, num_of_delayed_payment,
                                                         payment_behaviour, credit_utilization_ratio, delay_from_due_date,
                                                         changed_credit_limit, amount_invested_monthly, num_credit_card,
                                                         outstanding_debt, interest_rate, age_group, delay_group, credit_mix,
                                                         occupation, payment_of_min_amount)
        st.success(prediction_result)

        # Personalized Recommendation
        st.subheader("Personalized Recommendation")
        if float(prediction_result.split(": ")[1][:-1]) < 50.0:
            st.write("Your credit score is low. It is recommended to improve your credit history and manage your debts more effectively.")
        else:
            st.write("Your credit score is good. Keep maintaining good financial habits.")