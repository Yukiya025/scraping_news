# -*-coding:utf-8-*-
# https://github.com/calthoff/self_taught/blob/master/python_ex289.py/
import urllib2
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site
        
    def scrape(self):
        r = urllib2.urlopen(self.site) # urlopen関数を実行するとResponseオブジェクトが返される。
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)
                
news = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/"                
Scraper(news).scrape()        