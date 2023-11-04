import requests
import streamlit as st
import pandas as pd

import pickle
from pathlib import Path

import streamlit_authenticator as stauth  


#st.set_page_config(layout="wide",initial_sidebar_state="collapsed")
st.set_page_config(layout="wide")

st.title("Welcome to Meteo Australia's Rain Predictor!")
st.write("The model evaluates the probability of whether it will rain tomorrow in your city based on your input.")

# --- USER AUTHENTICATION ---
names = ["Alice in Wonderland", "Bob the Builder"]
usernames = ["alice", "bob"]
passwords = ["wonderland","builder"]

hashed_passwords=stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pwd.pkl"

with file_path.open("wb") as file:
    pickle.dump(hashed_passwords,file)

# load hashed passwords
file_path = Path(__file__).parent / "hashed_pwd.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "dashboard", "abcdef", cookie_expiry_days=0)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:         

    def user_input_features():
        B1 = st.sidebar.slider('Location',  0, 48,  35)
        B2 = st.sidebar.slider('Rainfall', 0.00, 2.00, 1.20)
        B3 = st.sidebar.slider('WindGustDir', 0, 15, 8)
        B4 = st.sidebar.slider('WindGustSpeed', 9, 67, 31)
        B5 = st.sidebar.slider('WindDir9am', 0, 15, 15)
        B6 = st.sidebar.slider('WindDir3pm', 0, 15, 9)
        B7 = st.sidebar.slider('WindSpeed9am', 0, 37, 7)
        B8 = st.sidebar.slider('WindSpeed3pm', 0, 39, 15)
        B9 = st.sidebar.slider('Humidity9am',  18, 100, 88)
        B10 = st.sidebar.slider('Humidity3pm', 1, 100, 91)
        B11 = st.sidebar.slider('Pressure3pm', 998.50, 1032.00, 1013.70)
        B12 = st.sidebar.slider('Temp3pm', 2.3, 40.7, 16.20)
        B13 = st.sidebar.slider('RainToday', 0, 1, 1)

        # Inputs to ML model
        global data
        data= {	"Location": B1,
        "Rainfall": B2,
            "WindGustDir": B3,
            "WindGustSpeed": B4,
            "WindDir9am": B5,
            "WindDir3am": B6,
            "WindSpeed9am": B7,
            "WindSpeed3am": B8,
            "Humidity9am": B9,
            "Humidity3am": B10,
            "Pressure3pm": B11,
            "Temp3pm": B12,
            "RainToday": B13 }            
                    
        user_input_features = pd.DataFrame(data, index=[0])
        return user_input_features 
    
    df = user_input_features()

    st.write('Welcome:', name)

    st.header('Input parameters')
    st.write(df)

    response = requests.post(f"http://localhost:8000/", json=data)
    prediction=response.text

    x=prediction
    st.write('Probability = ', x, '  (Threshold=0.5)')

    if prediction < '0.5': 
        st.write(":sunny: Dry weather!")
    else: 
        st.write(":confused: Sorry, it will rain tomorrow") 




#    col1, col2 = st.columns(2)
#    with col1:
        
#        if prediction < '0.2': 
#             st.header('L’interprétabilité locale')
#             st.image("local2.png")
#        elif prediction < '0.5': 
#             st.header('L’interprétabilité locale')    
#             st.image("http://localhost:8000/OK")   
#        else: 
#             st.header('L’interprétabilité locale')
#             st.image("http://localhost:8000/OK")	

#    with col2:
#            st.header('L’interprétabilité globale')
#            st.image("global1.png")



