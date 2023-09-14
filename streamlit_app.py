import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError


st.title('I am an early person 🐔')

st.header('learning to add a ine below the title')
st.text('adding first line below header')
st.text('adding second line')


my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected= st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
st.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
  

st.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = st.text_input('What fruit would you like information about?')
  if not fruit_choice:
    st.error("Please select a fruit to get information")
  else:
    back_from_function= get_fruityvice_data(fruit_choice)
    st.dataframe(back_from_function)
    
except URLError as e:
  st.error()
 
    
# st.write('The user entered ', fruit_choice)


# # st.text(fruityvice_response.json())


# # normalize the json output 
# fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# # display the normalised dataframe



st.stop()



my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
st.header("The fruit load list contains:")
st.dataframe(my_data_rows) 


add_my_fruit = st.text_input('What fruit would you like to add?','jackfruit')
st.write('Thanks for adding ', add_my_fruit)


my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')")
