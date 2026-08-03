import streamlit as st
import numpy as np

st.title("Checking for Eligibility to Vote")
age=st.text_input("enter your age")
if st.button("Submit"):
  if age >=18 :
    st.write("Eligible for vote")
  else:
    st.write("Not Eligible")

