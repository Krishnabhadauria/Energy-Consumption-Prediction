import streamlit as st
import pickle
import sklearn
import pandas as pd 
import numpy as np 

model = pickle.load(open('./model.sav','rb'))

st.title('Energy Consumption Prediction')
st.sidebar.header('Location Data')

def user_input():
    Temperature = st.sidebar.number_input("Temperature")
    Humidity = st.sidebar.number_input("Humidity")
    SquareFootage = st.sidebar.number_input("Square Footage")
    Occupancy = st.sidebar.slider('Occupancy', 1,50, 1)
    HVACUsage = st.sidebar.selectbox("HVAC Usage", [0, 1])
    LightingUsage = st.sidebar.selectbox("Lighting Usage", [0, 1])
    RenewableEnergy = st.sidebar.number_input("Renewable Energy")
    DayOfWeek = st.sidebar.slider('DayOfWeek', 0, 6, 1)
    Holiday	= st.sidebar.selectbox("Holiday", [0, 1])
    Year = st.sidebar.number_input("Year")
    Month = st.sidebar.number_input("Month")
    Day = st.sidebar.number_input("Day")
    Hour = st.sidebar.number_input("Hour")
    Minute = st.sidebar.number_input("Minute")
    Second = st.sidebar.number_input("Second")

    user_input_data = {
        'Temperature': Temperature,
        'Humidity': Humidity,
        'SquareFootage': SquareFootage,
        'Occupancy': Occupancy,
        'HVACUsage': HVACUsage,
        'LightingUsage': LightingUsage,
        'RenewableEnergy': RenewableEnergy,
        'DayOfWeek': DayOfWeek,
        'Holiday': Holiday,
        'Year': Year,
        'Month': Month,
        'Day': Day,
        'Hour': Hour,
        'Minute': Minute,
        'Second': Second    
    }    

    user_input = pd.DataFrame(user_input_data, index=[0])
    return user_input

user_data= user_input()
st.header('User Data')
st.write(user_data)

consumption=model.predict(user_data)
st.subheader('Energy Consumption:')
st.subheader(consumption[0])