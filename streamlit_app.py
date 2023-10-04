import streamlit

streamlit.title('My parents new healthy dinner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
                                
my_fruit_list = my_fruit_list.set_index('Fruit') 

streamlit.multiselect("Pick Some Fruit:",list(my_fruit_list.index)) 

streamlit.dataframe(my_fruit_list)

streamlit.header("Fruityvice")

import requests

responce = requests.get("https://fruityvice.com/api/fruit/watermelon")

normalize = pandas.json_normalize(responce.json())

streamlit.dataframe(normalize)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
