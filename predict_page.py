import streamlit as st
import pickle
import numpy as np
import pandas as pd

def model():
    with open('xgbregressor_model.pkl','rb') as file:
       data=pickle.load(file)
    return data

data=model()

def prediction():
    st.title("Housing Price Prediction")
    st.write("""Entering information manually helps us predict accuracy of 86.6% !""")

def get_user_input():
    discrete_num_features=['number of bedrooms', 'number of bathrooms', 'grade of the house']

    age_features=['Built Year', 'Renovation Year','House Age']

    continuous_num_features=['living area', 'lot area', 'number of floors', 
                  'number of views', 'Area of the house(excluding basement)', 'Area of the basement', 
                   'Lattitude', 'Longitude', 'Provided Area', 'lot_area_renov', 
                  'Number of schools nearby', 'Distance from the airport' ]
    
    cat_features=['waterfront present','condition of the house']


    user_inputs={}
    st.sidebar.header("Input features")
    for i in discrete_num_features:
        user_inputs[i]=st.sidebar.slider(i, min_value=1, max_value=10, value=1)

    for i in continuous_num_features:
        user_inputs[i]=st.sidebar.number_input(f"Enter {i}", value=0)

    for i in age_features:
        user_inputs[i]=st.sidebar.number_input(f"Enter {i}", value=0)

    for i in cat_features:
        if i=='waterfront present':
            options = ["Yes", "No"]
        else:
            options=["Meagre","Moderately Degraded", "Fair","Good State", "Excellent State"]

        user_inputs[i] = st.sidebar.selectbox(f"Select {i}", options)
    user_input_df = pd.DataFrame([user_inputs])
    return user_input_df

def main():
    user_input_df=get_user_input()

    st.subheader("User Input:")
    st.write(user_input_df)

    if st.button("Predict"):
        prediction = data.predict(user_input_df)
        st.subheader("Prediction:")
        st.write(prediction[0])




