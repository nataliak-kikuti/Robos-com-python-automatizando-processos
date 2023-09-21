import chromedriver_binary
from selenium import webdriver
import time

class roboYoutube():
    def __int__(self):
        self.webdriver = webdriver.Chrome()


    def busca(self, busca):
        url = "https://www.youtube.com/results?search_query=%s" % busca
        self.webdriver.get(url)

bot = roboYoutube()
bot.busca("teste")