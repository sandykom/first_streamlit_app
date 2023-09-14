import streamlit as st
st.title('I am an early person 🐔')

st.header('learning to add a ine below the title')
st.text('adding first line below header')
st.text('adding second line')


import pandas as pd
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

# Display the table on the page.
st.dataframe(my_fruit_list)
