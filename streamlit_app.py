import streamlit as st
st.title('I am an early person 🐔')

st.header('learning to add a ine below the title')
st.text('adding first line below header')
st.text('adding second line')


import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.dataframe(my_fruit_list)
