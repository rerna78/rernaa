import pickle
import streamlit as st

diabetes_model =pickle.load(open('diabetes_model.sav', 'rb'))
st.title('Data Mining Prediksi Diabetes')

col1, col2 = st.columns(2)

with col1:

 Pregnancies = st.text_input('Input Nilai Pregnancies')

with col2:
 Glucose = st.text_input('Input Nilai Glucose')

with col1:
 BloodPressure = st.text_input('Input Nilai Blood Pressure')

with col2:
 SkinThickness = st.text_input('Input Nilai SkinThckness')

with col1:
 Insulin = st.text_input('Input Nilai Insulin')

with col2:
 BMI = st.text_input('Input Nilai BMI')

with col1:
 DiabetesPedigree = st.text_input('Input nilai Diabetes Pedigree Function')

with col2:
 Age = st.text_input('Input nilai Age')

diab_diagnosis = ''

if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigree, Age,]])
    
    if(diab_prediction[0]== 0):
      diab_diagnosis = 'Pasien terkena Diabetes'
    else:
      diab_diagnosis = 'Pasien tidak terkena Diabetes'

st.success(diab_diagnosis)

