from selenium import webdriver


class BasePage:
    def __init__(self,driver=None):
        #如果发现drvier没有值，说明第一次实例化子类
        if driver is None:
            self.driver = webdriver.Chrome()
        #如果发现有值，说明不是第一次实例化
        else :
            self.driver = driver