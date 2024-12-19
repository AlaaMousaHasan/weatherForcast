import os
import logging
import configparser
from datetime import datetime
from fetch_data import FetchData
from important_data import ImportantData
from email_sender import EmailSender
from pdf import PDFGenerator  

# Ensure the logs directory exists
log_dir = "logging"
os.makedirs(log_dir, exist_ok=True)

# Create a timestamped log file in the "logging" folder
log_filename = os.path.join(log_dir, f"weather_script_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_filename),  
        logging.StreamHandler()  
    ]
)


logger = logging.getLogger("Main")


# Function to read configuration from config.txt
def read_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    
    # Read API key from the config file
    api_key = config.get('API', 'api_key')
    
    # Read email credentials from the config file
    sender_email = config.get('EMAIL', 'sender_email')
    sender_password = config.get('EMAIL', 'sender_password')
    recipient_email = config.get('EMAIL', 'recipient_email')

    return api_key, sender_email, sender_password, recipient_email



def main():
    config_file = 'config.txt'  
    
    # Read the API key and email settings from the config file
    API_KEY, SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL = read_config(config_file)
    LOCATION = 'Berlin'

    try:
        # Step 1: Fetch weather data
        logger.info(f"Fetching weather data for {LOCATION}")
        weather_fetcher = FetchData(API_KEY)
        forecast_data = weather_fetcher.parse(LOCATION)

        # Step 2: Extract important data
        logger.info("Extracting important weather data")
        important_data_extractor = ImportantData(forecast_data)
        formatted_data = important_data_extractor.parse()

        # Step 3: Generate the PDF with the formatted data
        logger.info("Generating PDF with weather data")
        pdf_generator = PDFGenerator()
        pdf_filename = pdf_generator.generate_pdf(formatted_data)

        # Step 4: Send the email with the PDF attachment
        logger.info(f"Sending email to {RECIPIENT_EMAIL}")
        email_sender = EmailSender(SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAIL)

        # Construct the message body
        message_body = (
            'Good Morning Lisa   \n'
            '   \n'
            '14-Day Weather Forecast for Berlin\n'
            'Please find the attached 14-day weather forecast for Berlin.\n'
            ' \n'
            'Have a nice day'
        )

        # Send the email
        email_sender.send_email_with_pdf(
            'Weather forcast',
            message_body,
            pdf_filename
        )

        logger.info("Weather data successfully fetched, PDF generated, and email sent")

    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)


if __name__ == "__main__":
    main()
