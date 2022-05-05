import datetime as dt
import pandas
import random
import smtplib

now = dt.datetime.now()
today = (now.month, now.day)
my_email = "email here"
my_password = "password here"

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


if today in birthdays_dict:
    birthday_name = birthdays_dict[today]["name"]
    birthday_email = birthdays_dict[today]["email"]
    chosen_letter = random.randint(1, 3)
    with open(f"letter_templates/letter_{chosen_letter}.txt") as file:
        text = file.read()
        named_letter = text.replace("[NAME]", birthday_name)
    with smtplib.SMTP("INSERT SMTP HERE") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_email,
            msg=f"Subject:Happy Birthday!\n\n {named_letter}"
        )




