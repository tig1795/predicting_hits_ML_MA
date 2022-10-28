# https://medium.com/@traviscroyce/scraping-data-from-dynamic-websites-with-selenium-and-python-f702bb534974

from email import parser
from lib2to3.pgen2 import driver
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time 
import datetime
import os

url = 'https://www.billboard.com/charts/hot-100-song/'

driver = webdriver.Safari()
driver.get(url)
src = driver.page_source
parser = BeautifulSoup(src, 'lxml')
table = parser.find("div", attrs={"class":"chart-results-list // u-padding-b-250"})

song_titles = table.find_all('h3')
songlist =[h.text.strip() for h in song_titles[0:]]
songlist