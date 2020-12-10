import pandas as pd
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

    
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

# exporting the dataframe object as an excel sheet named output.xlsx and sheet name covid_19_stats
df.to_excel("output.xlsx",sheet_name='covid_19_stats')

# closes google chrome window
driver.quit()
