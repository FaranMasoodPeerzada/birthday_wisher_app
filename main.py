##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
import pandas as pd
import csv
MY_EMAIL="faranpeerzada253@gmail.com"
MY_PASSWORD="ucyvqjdtunotwjtk"
data = pd.read_csv("birthdays.csv")
with open('birthdays.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(["name","email", "year", "month","day"])
    writer.writerow(["Ash Ketchum", "English@yahoo.com","1993","4","10"])
    writer.writerow(["Gary Oak", "Mathematics@yahoo.com","1993","4","12"])
    writer.writerow(["Brock Lesner", "Physics@yahoo.com","1993","4","12"])
    writer.writerow(["Faran", "faranpeerzada253@yahoo.com","1993","3","11"])
# 2. Check if today matches a birthday in the birthdays.csv
import datetime as dt
now=dt.datetime.now()
month=now.month
day=now.day
today=(month,day)
birthday_dict={(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
import random
import smtplib
number=random.randint(1,3)
if today in birthday_dict:

    birthday_person=birthday_dict[today]
    name=birthday_person['name']

    file_path=f"letter_{number}.txt"
    with open(file_path,'r') as letter:
        contents=letter.read()
        new_mail=contents.replace('[NAME]',birthday_person['name'])
        print(birthday_person['name'])
# 4. Send the letter generated in step 3 to that person's email address.

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person['email'], msg=f"Subject:Happy Birthday \n\n {new_mail}")



