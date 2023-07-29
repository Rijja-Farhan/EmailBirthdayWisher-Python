import smtplib
import datetime as dt
import random
import pandas
import string

#  setting the email and password of the sender
my_email = "rijjatest@gmail.com"
password = "blxvbozvmgrfpvty"

#check today's date and month
now = dt.datetime.now()
today = now.day
this_month = now.month
#read the data of birthdays
data = pandas.read_csv("birthdays.csv")
#find the dates and months which are present in the birthdays data
date = [birthdays for birthdays in data["day"]]
months = [birthdays for birthdays in data["month"]]

#----- finding birthdays
#check if today's date and month are in birthdays date and month
if today in date and this_month in months:
    #if so then content is the data of the person whose birthday is today
    content = data[(data["month"] == this_month) & (data["day"] == today)]
    print(content)
    num = random.randint(1,3)#to find a random letter file
    with open(file="./letters/letter_"+str(num)+".txt") as letter:
        lines = letter.readlines()
        lines = [line.strip() for line in lines]
        # Replace [NAME] with the actual name in each line
        lines = [line.replace('[NAME]', content["name"].values[0]) for line in lines]
        print(lines)



    #sending the email
    text = '\n'.join(lines)
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # for security from anyone who can intervene
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="rijja12347@yahoo.com",
                msg="Subject: Happy Birthday\n\n{}".format(text)
            )
