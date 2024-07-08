import streamlit as st

st.title('Uber pickups in NYC')

number = st.number_input("Insert a number")
st.write("The current number is ", number)