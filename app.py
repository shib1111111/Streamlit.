import streamlit as st
import pandas as pd
st.write('Division of Two Numbers')
st.header("Enter the Two Numbers")
number1 = st.number_input("Enter the 1st Number",min_value=1)
number2 = st.number_input("Enter the 2st Number",min_value=0)
division = number2/number1
st.write('Division of Two Number are : ')
st.write(division)
