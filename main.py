from smtplib import SMTP
from datetime import datetime
from random import randint
from pandas import read_csv

GMAIL = "ntouchtongarbage@gmail.com"
YAHOO = "ntouchtongarbage@yahoo.com"

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

BIRTHDAY_LIST = read_csv("birthdays.csv")

print(BIRTHDAY_LIST["year"][0])

IS_BIRTHDAY = True

NOW = datetime.now()

VALID_YEAR = BIRTHDAY_LIST[BIRTHDAY_LIST.year == NOW.year]
VALID_MONTH = VALID_YEAR[BIRTHDAY_LIST.month == NOW.month]
VALID_DAY = VALID_MONTH[BIRTHDAY_LIST.day == NOW.day]

# 3. If step 2 is true, pick a random letter from letter templates
    # and replace the [NAME] with the person's actual name from birthdays.csv

LETTER_NUMBER = randint(1, 3)
with open(f"letter_templates/letter_{LETTER_NUMBER}.txt", mode="r") as file:
    letter = file.read()
    letter = letter.replace("[NAME]", "Bleh")
    # Next time I need to write the code to replace the name with the name from the CSV.
    print(letter)

# 4. Send the letter generated in step 3 to that person's email address.

# NOW = datetime.now()
# with open("quotes.txt", mode="r") as file:
#     lines = file.readlines()
#     QUOTE = choice(lines)

# if NOW.weekday() == 5:
#     with SMTP("smtp.gmail.com", port=587) as connection:
#         connection.starttls()
#         connection.login(
#             user=GMAIL,
#             password="tritxyfgglkzhmwv"
#         )
#         connection.sendmail(
#             from_addr=GMAIL,
#             to_addrs=YAHOO,
#             msg=f"Subject:Motivational quote of the week\n\n{QUOTE}"
#         )
