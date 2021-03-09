import bs4
from bs4 import BeautifulSoup
import pandas as pd


from selenium import webdriver
import time as t
import requests

data = pd.read_csv('duplicate_free_41K.csv')
truncat = data[:30000]
truncat = truncat.to_numpy()

webpage = "https://www.imdb.com/find?s=tt&q="
plots = []
for i in range(3):
    movie_name = truncat[i][2]
    query = str(movie_name)
    query = query.replace(" ", "")
    temp = webpage+query
    link = temp + "&ref_=nv_sr_sm"
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.get(url=link)
    driver.find_element_by_css_selector("""#main > div > div.findSection > table > tbody > tr:nth-child(1) > td.result_text > a""").click()
    url = driver.current_url
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    trun = soup.find("div", class_="summary_text").extract()
    plots.append(trun)
    driver.close()
print(plots)

