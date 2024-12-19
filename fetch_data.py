import requests
import logging
from parse_interface import ParseInterface

# Set up a logger for FetchData
logger = logging.getLogger("FetchData")

class FetchData(ParseInterface):


    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.weatherapi.com/v1/forecast.json"
    


    def parse(self, location):
        """Fetches weather data from the API"""


        url = f"{self.base_url}?key={self.api_key}&q={location}&days=14&aqi=no&alerts=no" # change the 14 to get less days 
        
        try:
            logger.info(f"Sending request to WeatherAPI for location: {location}")
            response = requests.get(url)
            
            if response.status_code == 200:
                logger.info("Weather data fetched successfully")
               
                parsedData = response.json()
                #print(parsedData)
                return parsedData  # Return the parsed data
            else:
                logger.error(f"Error fetching data: {response.status_code}")
                raise Exception(f"Error fetching data: {response.status_code}")

        except Exception as e:
            logger.error(f"An error occurred during API request: {e}", exc_info=True)
            raise
