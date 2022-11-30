import streamlit as st
import pandas as pd

st.title('Division of Two Numbers')
st.write("---")
st.header("Enter the Two Numbers")

number1 = st.number_input(label= "Enter the 1st large Number")
number2 = st.number_input(label= "Enter the 2st small Number")
st.write(div)
def div(): 
  if number2!=0:
        ans = num1 / num2
  else:
    st.warning("Division by 0 error. Please enter a non-zero number.")
    ans = "Not defined"
  st.success(f"Division of Two Number are :  {ans}")
if st.button("Calculate result"):
    div()
