from smtplib import SMTP
from datetime import datetime
from random import randint
from pandas import read_csv

GMAIL = "youremailherem"
YAHOO = "youremailhere"

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

BIRTHDAY_LIST = read_csv("birthdays.csv")

# print(BIRTHDAY_LIST["year"][0])

IS_BIRTHDAY = True

NOW = datetime.now()

VALID_MONTH = BIRTHDAY_LIST[BIRTHDAY_LIST.month == NOW.month]
VALID_DAY = VALID_MONTH[BIRTHDAY_LIST.day == NOW.day]
if len(VALID_DAY) == 0:
    IS_BIRTHDAY = False

# 3. If step 2 is true, pick a random letter from letter templates
    # and replace the [NAME] with the person's actual name from birthdays.csv

LETTER_NUMBER = randint(1, 3)
with open(f"letter_templates/letter_{LETTER_NUMBER}.txt", mode="r") as file:
    letter = file.read()
    new_name = VALID_DAY.name
    new_name = new_name.to_string(index=False)
    letter = letter.replace("[NAME]", new_name)

# 4. Send the letter generated in step 3 to that person's email address.

if IS_BIRTHDAY:
    with SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(
            user=GMAIL,
            password="Put password here"
        )
        connection.sendmail(
            from_addr=GMAIL,
            to_addrs=YAHOO,
            msg=f"Subject:Happy Birthday!\n\n{letter}"
        )
