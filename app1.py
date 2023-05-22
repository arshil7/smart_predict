import streamlit as st
from joblib import load
import numpy as np


def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://www.bhf.org.uk/-/media/news-images/2021/march/ai-heart-tool-640x410px.jpg?h=65%25&w=100%25&rev=c51b0b8af9d64101997bfd9252fb04a2&hash=D22AFDC9BCB488C861CFB81D348FCA33");
             background-attachment: fixed;
             background-size: small
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

def load_model(model_file):
    model = load(model_file)
    return model

def predict(model, sex=0, age=0, cp=0, trestbps=0, chol=0, fbs=0, restecg=0, thalach=0,	exang=0, oldpeak=0,	slope=0, ca=0, thal=0):
    x = np.array([[sex, age, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak,	slope, ca, thal]])
    y = model.predict(x)
    return y[0] # reutrn fist elemnt of array

st.title("Heart Disease Prediction  :hospital: ")

with st.form(key='my_form'):
    col1,col2,col3 = st.columns(3)
    with col1:
        age = st.number_input(label='Age', value=1, min_value=1, step=10)

    with col2:
        sex = st.number_input(label='Sex[0-Female, 1-Male]', value=0, min_value=0, max_value=1)

    with col3:
        cp = st.number_input(label='Chest Pain Type''[0,1,2,3]', value=0, min_value=0, max_value=3)

    trestbps = st.slider(label='Trestbps resting blood pressure (in mm Hg on admission to the hospital)', value=1, min_value=0, max_value=1000)
    chol = st.slider(label='Chol serum cholestoral in mg/dl', value=1, min_value=0, max_value=1000)

    col3,col4 = st.columns(2)
    with col3:
        fbs = st.number_input(label='FBS (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)', value=1, min_value=0, max_value=1)
    
    with col4:
        restecg = st.number_input(label='Restecg  [resting electrocardiographic results]', value=1, min_value=0, max_value=2)
    
    thalach = st.slider(label='Thalach [maximum heart rate achieved]', value=1, min_value=0, max_value=500)

    col5,col6,col7 = st.columns(3)
    with col5:
        exang = st.number_input(label='Exang [exercise induced angina (1 = yes; 0 = no)]', value=1, min_value=0, max_value=1)
        
    with col6:
        oldpeak = st.number_input(label='Oldpeak [ST depression induced by exercise relative to rest]', value=1.0, min_value=0.0, max_value=4.0, step=0.1)

    with col7:
        slope = st.number_input(label='Slope [the slope of the peak exercise ST segment]', value=1, min_value=0)

    col8,col9 = st.columns(2)
    with col8:
        ca = st.number_input(label='Ca [number of major vessels (0-3)]', value=1, min_value=0, max_value=3, step=1)

    with col9:
        thal = st.number_input(label='Thal', value=1, min_value=0)
    
    submit_button = st.form_submit_button(label='Predict')
   

if submit_button:
    model = load_model('heart_pre.joblib')
    target = predict(model, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal )
if target == 0:
    st.success(f'You dont have Heart Disease! :thumbsup:')
else:
    st.error('You have Heart Disease :thumbsdown:')


