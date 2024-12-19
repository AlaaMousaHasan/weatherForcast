import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class EmailSender:
    def __init__(self, sender_email, sender_password, recipient_email):
        self.sender_email = sender_email
        self.sender_password = sender_password
        self.recipient_email = recipient_email
    
      # Method to send email with PDF attachment
    def send_email_with_pdf(self, subject, message_body, pdf_filename):
        # Set up the MIME structure of the email
        msg = MIMEMultipart()
        msg['From'] = self.sender_email
        msg['To'] = self.recipient_email
        msg['Subject'] = subject
        # msg['Cc'] = self.cc_email  # Add CC header if needed

        # Attach the body of the email
        msg.attach(MIMEText(message_body, 'plain'))

        # Attach the PDF file
        with open(pdf_filename, "rb") as attachment:
            # application: a general binary application file.
            # octet-stream: raw binary data.
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())

            encoders.encode_base64(part)  # encoding for email is needed

            part.add_header('Content-Disposition', f'attachment; filename= {pdf_filename}')
            msg.attach(part)  # add it to the email.

        # Set up the SMTP server
        try:
            srv = smtplib.SMTP('smtp.gmail.com', 587)  # Gmail server, TLS protocol 587
            srv.starttls()  # Use TLS for secure connection
            srv.login(self.sender_email, self.sender_password)
            
            # Send the email
            srv.send_message(msg)
            print(f"Email sent to {self.recipient_email} with PDF attachment")
        except Exception as e:
            print(f"Failed to send email: {e}")
        finally:
            srv.quit()  # Stop the server.

