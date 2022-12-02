from smtplib import SMTP

GMAIL = "ntouchtongarbage@gmail.com"
YAHOO = "ntouchtongarbage@yahoo.com"

with SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=GMAIL, password="tritxyfgglkzhmwv")
    connection.sendmail(
        from_addr=GMAIL,
        to_addrs=YAHOO,
        msg="Subject:Hello\n\nThis is the body."
    )
