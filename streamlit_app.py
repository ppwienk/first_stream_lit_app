import streamlit
import pandas

streamlit.header('menu')
streamlit.text('friet')
streamlit.text('kroket')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)


