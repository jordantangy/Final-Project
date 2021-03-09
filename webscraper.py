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
for i in range(6):
    # take the movie name from database
    movie_name = truncat[i][2]
    #turn it into a string
    query = str(movie_name)
    # remove spaces
    query = query.replace(" ", "")
    # add components to create a working web address
    temp = webpage+query
    link = temp + "&ref_=nv_sr_sm"
    # declare chrome driver and get the url
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    driver.get(url=link)
    # click on the first movie on the page
    driver.find_element_by_css_selector("""#main > div > div.findSection > table > tbody > tr:nth-child(1) > td.result_text > a""").click()
    # get the url of the current web page
    url = driver.current_url
    # get the page and parse it into html
    page = requests.get(url)
    soup = BeautifulSoup(url.content, 'html.parser')
    # exctract the plot and insert it into the plots array
    plot = soup.find("div", class_="summary_text").extract()
    plots.append(plot)
    # close the page
    driver.close()
print(plots)


