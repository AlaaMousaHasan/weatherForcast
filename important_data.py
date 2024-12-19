from datetime import datetime
import logging
from parse_interface import ParseInterface

# Set up a logger for ImportantData
logger = logging.getLogger("ImportantData")

class ImportantData(ParseInterface):

    def __init__(self, forecast_data):
        self.forecast_data = forecast_data
        self.formatted_data = ""



    def parse(self):
        """Extracts and formats important data"""
        try:
            logger.info("Extracting data from weather forecast")
            forecast_days = self.forecast_data['forecast']['forecastday']
            #print(forecast_days)
            for day in forecast_days:
                day_str = day['date'] # date extracting
                #print(day_str)
                day_obj = datetime.strptime(day_str, '%Y-%m-%d')  # Convert string to datetime object
                #print(day_obj)
                wkday = day_obj.strftime('%A') # %a for a short name e.g Fri 
                #print(wkday)
                max_temp = day['day']['maxtemp_c']
                min_temp = day['day']['mintemp_c']
                rain = day['day']['daily_chance_of_rain']
                wind = day['day']['maxwind_kph']
                
                self.formatted_data += f"""
                                        Date: {day_str} ({wkday})
                                        Max Temp: {max_temp}°C, Min Temp: {min_temp}°C
                                        Chance of Rain: {rain}%
                                        Wind Speed: {wind} km/h
                                        ############################################################
                                        """
        
            logger.info("Data extraction and formatting successful")
            return self.formatted_data

        except Exception as e:
            logger.error(f"An error occurred during data extraction: {e}", exc_info=True)
            raise
