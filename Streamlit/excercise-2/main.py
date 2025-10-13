import streamlit as st
import datetime as dt

today = dt.date.today()

st.title("Age Calculator")

st.subheader("Calculate your age with our Program")

dob = st.date_input("Date of Birth", None ,min_value=dt.date(1925, 1, 1), max_value="today")

if dob:
    st.text(f"Great your Date of Birth is '{dob}'")
    
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

    st.info(f"You are {age} years old")
    
    if (today.day == dob.day) and (today.month == dob.month):
        st.success("Its Your Birthday Today🥳🥳")
