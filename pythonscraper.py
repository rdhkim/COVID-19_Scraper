import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import smtplib
    
# Setting chromedriver file path
chromedriver = '/Users/ryankim/Downloads/chromedriver'

# creating driver object and locating the chromedriver file to be executed
driver = webdriver.Chrome(chromedriver)

# opening a google chrome window on the Ontario COVID-19 webpage
driver.get("https://www.ontario.ca/page/how-ontario-is-responding-covid-19")

# Setting options for our chrome browser
options = webdriver.ChromeOptions()
options.page_load_strategy = 'eager'
options.add_argument('headless')

# takes a 10 second pause to allow all element data to appear on the screen
driver.implicitly_wait(10)

# finding the table element tag on the webpage (contains the data about % increase in cases; first table | table[1])
table = driver.find_element_by_xpath('//*[@id="pagebody"]/table[1]')

# creating pandas dataframe object to export as excel file
all_tables = pd.read_html(driver.page_source, attrs={'class': 'numeric full-width'})
df = all_tables[0]
percent_change, direction_change = df.iloc[1]['Percentage'].split('%')
print(percent_change + direction_change)

# closes google chrome window
driver.quit()

if float(percent_change) > 0.01 and str(direction_change) == ' increase':
    #email code
    FROM = "ryan.k0223@gmail.com"
    TO = ["ryan.k0223@gmail.com"]
    SUBJECT = "Covid-19 5% increase in cases since yesterday"
    BODY = "Covid-19 cases in Ontario have increased by " + percent_change +" since yesterday/"
    message = 'Subject: '+SUBJECT + '\n\n' +BODY
    
    # Send the mail
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("username@gmail.com", "password")
    server.sendmail(FROM, TO, message)
    server.quit()