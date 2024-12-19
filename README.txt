
Weather Forecast Script

Project Description
This project automates the process of fetching a 14-day weather forecast for a specific location, formatting the weather data, generating a PDF with the formatted information, and sending that PDF as an email attachment. The project is structured into several Python classes that handle different tasks such as fetching data, formatting it, generating PDFs, and sending emails.

The project uses:
- WeatherAPI to get the weather data.
- FPDF to generate PDFs.
- SMTP to send the email.


Python Files:
- fetch_data.py: Contains the FetchData class, which fetches the 14-day weather forecast.
- important_data.py: Contains the ImportantData class, which extracts and formats the relevant weather data.
- interface.py: interface used by fetchdate and importantdata
- pdf.py: Contains the PDFGenerator class, which generates a PDF from the formatted weather data.
- email_sender.py: Contains the EmailSender class, which sends an email with the PDF attached.
- main.py: The main script that ties everything together: fetching data, generating the PDF, and sending the email.

Configuration File:
- config.txt: A file where you store your email credentials and the recipient's email in an easy-to-edit format.

Batch File:
- schudler.bat: A batch file to run the Python script and schedule it with Windows Task Scheduler.

Requirements
Before running the script, make sure you have the following:
1. Python installed (preferably version 3.x).
2. Required Python libraries:
   - requests
   - fpdf
   - smtplib
   - configparser

Install them via pip:

pip install requests fpdf

Setup Instructions

1. Weather API Key
- Sign up at WeatherAPI (https://www.weatherapi.com/) to get an API key.
- Replace API_KEY in config.txt with your actual API key.

2. Email Configuration
- You need to provide email credentials and recipient details in config.txt:

config.txt

[api]
api_key=yourAPI

[EMAIL]
sender_email=your-email@gmail.com
sender_password=your-app-password
recipient_email=recipient-email@gmail.com

Important:
- Make sure to use an App Password instead of your regular email password for Gmail (or similar email services). You can generate app passwords in your email provider's account settings.

3. Batch File Setup (schudler.bat)
.bat file to run the Python script. The file contents should look like this:


This batch file will run your Python script (main.py) from the directory it's located in.

4. Running the Script

Manually:
- You can run the script manually by executing the schudle.bat file. This will fetch the weather data, generate the PDF, and send the email.

double-click schudle.bat

Automatically with Windows Task Scheduler:
You can schedule the script to run automatically using Windows Task Scheduler.

1. Open Task Scheduler by pressing Windows + R, typing taskschd.msc, and pressing Enter.
2. Click Create Basic Task in the right panel.
3. Give the task a name (e.g., "Weather Script Scheduler") and set how often you want the script to run (e.g., daily at 7 AM).
4. Select Start a Program for the action and browse to your schudler.bat file.
5. In the final window, review the details and click Finish.
