from bs4 import BeautifulSoup as Soup
from selenium import webdriver
import csv
f = open('daum.csv','w', newline='')
wr = csv.writer(f)

driver = webdriver.Chrome('chromedriver.exe')
page = "1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20"
page_list = page.split(",")

for n in page_list :
    driver.get("https://news.daum.net/breakingnews/society"+n+"")

    html = driver.page_source
    soup = Soup(html, 'html.parser')

    news_header = soup.select('#newsColl > div.cont_divider > ul > li > div.wrap_cont > a')

    for i in news_header :
        print(i.text)
        wr.writerow([i.text])

