import streamlit as st
import numpy as np

st.title("Age validation for vote")
age=st.number_input("Enter your age:")
if st.button("submit"):
  if age>=18:
    st.success("you are eligible to vote")
  else:
    st.write("you are not eligible to vote")
