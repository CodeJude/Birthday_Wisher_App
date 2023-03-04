import pandas
from datetime import datetime
import smtplib
import random

MY_EMAIL = "MY_EMAIL"
PASSWORD = "PASSWORD"
receiver_email = "test@yahoo.com"

today = (datetime.now().month, datetime.now().day)
data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

print(today)
print(birthday_dict)

if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday!\n\n"
                                                                                       f"{contents}")
