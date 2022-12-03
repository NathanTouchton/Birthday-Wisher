from smtplib import SMTP
from datetime import datetime
from random import choice

GMAIL = "ntouchtongarbage@gmail.com"
YAHOO = "ntouchtongarbage@yahoo.com"

NOW = datetime.now()
with open("quotes.txt", mode="r") as file:
    lines = file.readlines()
    QUOTE = choice(lines)

if NOW.weekday() == 5:
    with SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(
            user=GMAIL,
            password="tritxyfgglkzhmwv"
        )
        connection.sendmail(
            from_addr=GMAIL,
            to_addrs=YAHOO,
            msg=f"Subject:Motivational quote of the week\n\n{QUOTE}"
        )
