from smtplib import SMTP

gmail = "ntouchtongarbage@gmail.com"

connection = SMTP("smtp.gmail.com")
connection.starttls()
