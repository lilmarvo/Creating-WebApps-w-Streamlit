import streamlit as st
import pandas

data = {
  'Series_1': [1,3,5,7,9],
  'Series_2': [10,40,80,160,250],
  'Series_3': [25,55,65,95,115]
}

df = pandas.DataFrame(data)

st.title('My first streamlit App')
st.subheader('Introduction to Steamlit: Automate it all')
st.write('''This is my first Web App. Enjoy it!''')
st.write(df)

st.line_chart(df)

mySlider = st.slider('Celsius')
st.write(mySlider, 'in Fahrenheit is',  mySlider * 9/5 + 32)