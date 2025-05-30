import streamlit as st
import requests
import numpy as np
import pandas as pd
import datetime

'''
# TaxiFare prediction front
'''


d = st.date_input(
    "Input date: ",
    datetime.date(2014,7,6))
st.write('You input this as date:', d)

t = st.time_input(
    "Input time: ",
    datetime.time(19,18))
st.write("You input this as time:", t)

input_dt = f"{d} {t}"

p_long = float(st.number_input('Insert the pickup longitude',-73.950655,format="%0.1111111f"))

st.write('The pickup longitude ', p_long)

p_lat = float(st.number_input('Insert the pickup latitude',40.783282,format="%0.1111111f"))

st.write('The pickup latitude ', p_lat)

d_long = float(st.number_input('Insert the dropoff longitude',-73.984365,format="%0.1111111f"))

st.write('The dropoff longitude ', d_long)

d_lat = float(st.number_input('Insert the dropoff latitude',40.769802,format="%0.1111111f"))

st.write('The dropoff latitude ', d_lat)

n_passengers = int(st.number_input('Insert the number of passengers',2))

st.write('The number of passengers ', n_passengers)

lw_url = 'https://taxifare.lewagon.ai/predict'

url = "https://taxifare-299294999012.europe-west1.run.app/predict"

params = {"pickup_datetime": input_dt,  # 2014-07-06 19:18:00
        "pickup_longitude": p_long,    # -73.950655
        "pickup_latitude": p_lat,     # 40.783282
        "dropoff_longitude": d_long,   # -73.984365
        "dropoff_latitude": d_lat,    # 40.769802
        "passenger_count": n_passengers
}
response = requests.get(url,params=params)

response = response.json()

predicted_fare = round(response["fare"],2)

"""
##  Let's predict the fare for your taxi ride
"""

st.write(f"The predicted fare is from your API is ${predicted_fare}")
