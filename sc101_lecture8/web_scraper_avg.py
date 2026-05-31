"""
File: web_scraper_avg.py
Name:
--------------------------
This program demonstrates how to scrape data from
www.imdb.com/chart/top
and compute average ratings.

By collecting the scores of the top 250 movies,
we use Python to calculate and find out their
overall average rating.
"""

import requests 
from bs4 import BeautifulSoup


def main():
	url = 'http://www.imdb.com/chart/top'
	response = requests.get(url)
	html = response.text
	soup = BeautifulSoup(html)
	#########################
	#                       #
	#         TODO:         #
	#                       #
	#########################


if __name__ == '__main__':
	main()
