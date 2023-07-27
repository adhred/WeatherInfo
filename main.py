import streamlit as st
from weather_app import ExampleAPIConnection

st.set_page_config(
    page_title='Weather App',
    page_icon='☁️'
)

# Create the ExampleAPI Connection
connection = st.experimental_connection('example_api_connection', type=ExampleAPIConnection)

# Fetch data from ExampleAPI
city = st.text_input("Enter the name of the city:", "London")

if city:
    data = connection.fetch_data(city)

    if data:
        st.write("## Weather Info for", city)
        st.write(f"Temperature: {data['temp']} degrees")
        st.write(f"Humidity: {data['humidity']} ")
        st.write(f"Wind Speed: {data['wind_speed']} m/s")
