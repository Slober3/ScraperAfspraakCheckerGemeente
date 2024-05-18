__author__ = '@Slober3'
__version__ = '0.1'

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from tkinter import Tk, Label

import sys
import os
import argparse
import re
import time

# Parse command line arguments
parser = argparse.ArgumentParser(description="Command line arguments")
parser.add_argument('-url',action='store', metavar='<website>', default='https://lier.mijnafspraakmaken.be/', help='The website to scrape')
args = parser.parse_args()

while True:
    # Set up the Selenium driver
    options = Options()

    # this parameter tells Chrome that
    # it should be run without UI (Headless)
    options.add_argument('--headless=new')

    # initializing webdriver for Chrome with our options
    driver = webdriver.Chrome(options=options)

    # Set the URL you want to scrape
    driver.get(args.url)
    # wait for the page to load
    driver.implicitly_wait(10)

    # Perform scraping operations using Selenium commands

    # click on  button with the text "Rijbewijs - voorlopig rijbewijs" use find_element to find the button
    driver.find_element("xpath",'//*[@id="activity-item-list"]/div[2]/ul/li[52]/button').click()
    # wait for the page to load
    driver.implicitly_wait(10)

    # click on the button with the text "Volgende" use find_element to find the button
    driver.find_element("xpath",'//*[@id="next-button"]').click()
    # wait for the page to load
    driver.implicitly_wait(10)

    # click on the button with the text "Volgende" use find_element to find the button
    driver.find_element("xpath",'//*[@id="next-button"]').click()
    # wait explicitly for the page to load
    driver.implicitly_wait(10)

    driver.find_element("xpath",'//*[@id="next-button"]').click()
    # wait explicitly for the page to load
    driver.implicitly_wait(10)

    # check if text "Geen beschikbare tijdstippen" is present on the page
    # get text and put it in variable
    getDate = driver.find_element("xpath",'//*[@id="container-fluid"]/main/div[1]/step-group-component/div[2]/div/appointment-date-time-component/div/table/tbody/tr/td[1]/label/span').get_attribute('innerHTML')
    driver.implicitly_wait(10)

    # Close the driver when you're done
    driver.quit()

    day_of_date = re.search(r'\d+', getDate).group()
    #check the value if it is smaller then 27  give me an alert also print out the current value)
    print("The day of the date is: " + day_of_date)

    title = "Alert!"
    message = "The day of the date is: " + day_of_date
    
    # Run the main loop to display the window
    if int(day_of_date) < 27:
        print("The day of the date is smaller than 27")
        root = Tk()
        root.state('zoomed')
        root.title(title)

        # Create a label with the message
        label = Label(root, text=message, font=("Arial", 65))
        label.pack()
        root.mainloop()


    time.sleep(60)
