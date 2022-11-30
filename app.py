import streamlit as st
import pandas as pd
st.write('Division of Two Numbers')
st.header("Enter the Two Numbers")
number1 = st.number_input("Enter the 1st large Number",step=1,format="%.2f")
number2 = st.number_input("Enter the 2st small Number",step=1,format="%.2f")
st.write(division)
def division(): 
  if number2!=0:
        ans = num1 / num2
    else:
        st.warning("Division by 0 error. Please enter a non-zero number.")
        ans = "Not defined"
   st.success(f"Division of Two Number are :  {ans}")
if st.button("Calculate result"):
    division()
