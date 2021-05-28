import streamlit as st
import datetime
import requests

st.markdown('''
# How much is my taxi fare in NY?
''')

pickup_longitude = st.text_input('pickup longitude?', 12)
pickup_latitude = st.text_input('pickup latitude?', 12)
dropoff_longitude = st.text_input('dropoff longitude?', 12)
dropoff_latitude = st.text_input('dropoff latitude?', 12)
passenger_count = st.slider('passengers?', 1, 4, 2)

d = st.date_input("Which day?", datetime.date.today())
t = st.time_input('Which time?', datetime.datetime.now().time())
pickup_datetime = str(d) + " " + str(t)

url = 'https://taxifare.lewagon.ai/predict'

params = {
    "pickup_datetime": pickup_datetime,
    "pickup_longitude": float(pickup_longitude),
    "pickup_latitude": float(pickup_latitude),
    "dropoff_longitude": float(dropoff_longitude),
    "dropoff_latitude": float(dropoff_latitude),
    "passenger_count": passenger_count
}

if st.button('calculate fare'):

    response = requests.get(url, params=params).json()

    fare = round(response["prediction"], 2)

    f'''
    Your fare will be {fare} USD
    '''

