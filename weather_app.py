import streamlit as st
from streamlit.connections import ExperimentalBaseConnection
import requests

class ExampleAPIConnection(ExperimentalBaseConnection):
    def _connect(self):
        self.api_key = st.secrets["api"]["api_key"]

    def fetch_data(self, city):
        api_url = f'https://api.api-ninjas.com/v1/weather?city={city}'
        headers = {'X-Api-Key': self.api_key}

        try:
            response = requests.get(api_url, headers=headers)
            if response.status_code == requests.codes.ok:
                data = response.json()
                return data
            else:
                st.error("Error occurred while fetching weather data.")
                return None
        except requests.exceptions.RequestException as e:
            st.error(f"Error occurred: {e}")
            return None
