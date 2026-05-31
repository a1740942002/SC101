"""
File: web_scraper_dynamically_loaded.py
Name:
--------------------------
This program demonstrates how to retrieve complete data
from a dynamically loaded webpage.

Using
www.imdb.com/chart/top
as an example, the program
shows how Python can be used to handle web pages whose
content is loaded dynamically rather than appearing
directly in the initial HTML.
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def main():
	driver = webdriver.Chrome()

	# Open the dynamic webpage
	driver.get('http://www.imdb.com/chart/top')

	# Wait for the page to load completely
	# Use explicit waits to wait for a specific element to be present
	try:
		element_present = EC.presence_of_element_located((By.ID, 'specific-element-id'))
		WebDriverWait(driver, 5).until(element_present)
	except TimeoutException:
		print("Timed out waiting for page to load")

	# Get the entire HTML content of the page
	html = driver.page_source
	###########################
	#                         #
	#    Your Codes Here      #
	#                         #
	###########################
	driver.quit()



if __name__ == '__main__':
	main()