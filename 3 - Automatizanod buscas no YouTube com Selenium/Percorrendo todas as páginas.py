import chromedriver_binary
from selenium import webdriver
import time

from selenium.webdriver.common.by import By


class roboYoutube():
    def __int__(self):
        self.driver = webdriver.Chrome()


    def busca(self, busca, paginas):
        videos = []
        pagina = 1
        url = "https://www.youtube.com/results?search_query=%s" % busca
        self.driver.get(url)
        while pagina <= paginas:
            titulos = self.driver.find_element(By.XPATH,'//*[@id="video-title"]/yt-formatted-string')

        for titulo in titulos:
            print("Video Encontrado: %s" % titulo.text)
            self.proxima_pagina()
            pagina += 1

    def proxima_pagina(self, pagina):
        print("Mudando para pagina %s" % (pagina+1))
        bottom = pagina * 10000
        self.driver.execute_script("window.scrollTo(0, %s);" % bottom)
        time.sleep(5)
        pass

bot = roboYoutube()
bot.busca("teste", 5)
