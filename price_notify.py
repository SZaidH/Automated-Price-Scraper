"""
Script that checks the DB and notifies the user incase the price of the item went down compared to the previous day
"""
import mysql.connector
import smtplib
import config

#DB Connection
mydb = mysql.connector.connect(
    host = config.HOST,
    user = config.USER,
    passwd = config.PASSWD,
    database = config.DATABASE
)

#send_email function is used for sending emails with the assistance of the smtplib library. Gmail is the selected email solution in this instance
def send_email(tomail, subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, tomail, message)
        server.quit()
        print("Success: Email sent!")
    except smtplib.SMTPException as exception:
        print("Failed: Email not sent!")
        print(exception)

#Email details
tomail = "" #Email ID which will recieve the price reduction notification
subject = "Price Alert"
msg = "The price of the item tracked has now reduced."

#SQL query to fetch the DB results and compare the last two records for price reduction
sqlCursor = mydb.cursor()
#Modify the tablename below
sqlCursor.execute("SELECT price from souq")
sqlResult = list(sqlCursor.fetchall())

if sqlResult[-1] < sqlResult [-2]:
    print("Item Discounted")
    send_email(tomail, subject, msg)
else:
    print("Not discounted")
