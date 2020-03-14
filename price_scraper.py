"""
Script that fetches price of an item from an ecommerce store
"""
import time
import mysql.connector
import config
from selenium import webdriver
from datetime import date

#Web Driver folder location 
chrome_path = r"" #Full Path of the webdriver required

#The Webdriver can be changed depending on the browser of your choice
driver = webdriver.Chrome(chrome_path)

#DB Connection
mydb = mysql.connector.connect(
    host = config.HOST,
    user = config.USER,
    passwd = config.PASSWD,
    database = config.DATABASE
)

#getPrice function utilizes the selenium library and extracts the price of the selected item with XPath
def getPrice(url):
    driver.get(url)

    #Enter the xpath of price element of the item. 
    #This can be achieved by going to the Dev tools of your browser of choice, inspecting the element containing the price, and then copying the XPath within the quotes below
    price = driver.find_element_by_xpath(""" """).text

    #Code blocks which extracts the numbers from strings. Modify the code according to your context
    final_price = price.split()
    time.sleep(10)
    driver.close()
    return final_price[0]

#insertData function inserts the extracted price and the current date to the DB 
def insertData(sql):
    sqlCursor = mydb.cursor()
    today = date.today()
    val = (pprice, today)
    sqlCursor.execute(sql, val)
    mydb.commit()
    message = print(sqlCursor.rowcount, "record inserted.")
    return message

#Enter the URL of the Item Page below
url = ""
pprice = getPrice(url)

#In this context, the table contains three columns: id(primary key, auto increment), price, date
#Modify the sql query below according to the structure of your DB
sql = "Insert into souq (price, pdate) values (%s, %s)"
insertData(sql)
