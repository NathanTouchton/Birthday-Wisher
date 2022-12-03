from smtplib import SMTP
from datetime import datetime
from random import choice
from pandas import read_csv

GMAIL = "ntouchtongarbage@gmail.com"
YAHOO = "ntouchtongarbage@yahoo.com"

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

BIRTHDAY_LIST = read_csv("birthdays.csv")

print(BIRTHDAY_LIST["year"][0])

IS_BIRTHDAY = True

NOW = datetime.now()
for item in BIRTHDAY_LIST.iterrows():
    print(BIRTHDAY_LIST.year)
    # if BIRTHDAY_LIST["year"][item] != NOW.year:
    #     IS_BIRTHDAY = False
    # print(BIRTHDAY_LIST["year"][item])

    # if BIRTHDAY_LIST["month"][item] != NOW.month:
    #     IS_BIRTHDAY = False

    # if BIRTHDAY_LIST["day"][item] != NOW.day:
    #     IS_BIRTHDAY = False

# print(IS_BIRTHDAY)

# 3. If step 2 is true, pick a random letter from letter templates
    # and replace the [NAME] with the person's actual name from birthdays.csv

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
