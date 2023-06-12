import pickle
import streamlit as st

# Membaca model
stunting_model = pickle.load(open('stunting_model.sav', 'rb'))

# Judul Web
st.title('Deteksi dini Stunting')

# Membagi 2 kolom

col1, col2 = st.columns(2)

with col1:
    Pregnancies = st.text_input('Input nilai Pregnancies')
with col2:
    Glucose = st.text_input('Input nilai Glucose')
with col1:
    BloodPressure = st.text_input('Input nilai Blood')
with col2:
    SkinThickness = st.text_input('Input nilai Skin')
with col1:
    Insulin = st.text_input('Input nilai Insulin')
with col2:
    BMI = st.text_input('Input nilai BMI')
with col1:
    DiabetesPedigreeFunction = st.text_input('Input nilai Diabetes')
with col2:
    Age = st.text_input('Input nilai Age')

# Coding untuk prediksi
stunting_diagnosis = ''

# Membuat tombol untuk prediksi

if st.button('Test Prediksi Stunting'):
    stunting_prediction = stunting_model.predict(
        [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if (stunting_prediction[0] == 1):
        stunting_diagnosis = 'Anak terindikasi Stunting'
    else:
        stunting_diagnosis = 'Anak tidak terindikasi'

st.success(stunting_diagnosis)
