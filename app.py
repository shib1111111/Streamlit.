import streamlit as st
import pandas as pd

st.title('Division of Two Numbers')
st.write("---")
st.header("Enter the Two Numbers")

number1 = st.number_input(label= "Enter the 1st Number")
number2 = st.number_input(label= "Enter the 2st Number")
if number2 != 0:
        ans = number1 / number2
else:
  st.warning("Division by 0 error. Please enter a non-zero number.")
  ans = "Not defined"



if st.button("Calculate"):
        st.write(f"Answer = {ans}")
        st.write("submitted by __")
        st.write("Shib Kumar Saraf ;/n",
                 "Email id : 21f1001520@student.onlinedegree.iitm.ac.in")

    
