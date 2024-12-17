import streamlit as st

st.title('Hitung Luas Segitiga')

alas = st.number_input ("Masukan Nilai Alas", 0)
tinggi = st.number_input ("Masukan Nilai Tinggi", 0)
hitung = st.button ("Hitung Luas")

if hitung :
    luas = 0.5 * alas * tinggi
    st.success (f"Luas segitiga adalah = {luas}")
