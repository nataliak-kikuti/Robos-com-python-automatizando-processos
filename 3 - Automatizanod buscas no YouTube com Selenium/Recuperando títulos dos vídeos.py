import chromedriver_binary
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


class roboYoutube():
    def __int__(self):
        self.driver = webdriver.Chrome()


    def busca(self, busca):
        url = "https://www.youtube.com/results?search_query=%s" % busca
        self.driver.get(url)
        titulos = self.driver.find_element(By.XPATH,'//*[@id="video-title"]/yt-formatted-string')
        for titulo in titulos:
            print("Video Encontrado: %s" % titulo.text)
bot = roboYoutube()
bot.busca("teste")