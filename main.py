# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib
import os

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

# Pick current date, month and day, in a tuple (month, day)
today = (datetime.now().month, datetime.now().day)

# Read the CVS file
data = pandas.read_csv("birthdays.csv")
# Convert it in a dictionary
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# Check if the current date is on dictionary
if today in birthdays_dict:
    birthdays_person = birthdays_dict[today]
    letter_path = f"letter_templates/letter_{randint(1, 3)}.txt"
# Reads a random letter
    with open(letter_path, 'r') as file:
        letter_to_send = file.read()
    letter_to_send = letter_to_send.replace("[NAME]", birthdays_person["name"])


email_to_send = birthdays_person["email"]

# Send the e-mail
with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs=email_to_send,
                        msg=f"Subject:Happy Birthday!\n\n{letter_to_send}"
                        )
