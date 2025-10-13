import streamlit as st

st.title("Programming Language Picker")
st.subheader("Java, Python, C++ and many more")
st.text("Pick Your Favourite Language")
choice = st.selectbox("Options: ", ['Python', 'C++', 'Java', 'Kotlin', 'Javascript', 'Ruby', 'C#', 'C', 'Typescript'])
st.write(f"{choice}, Nice Choice")
st.success("Selected!!")