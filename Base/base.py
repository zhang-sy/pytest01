from selenium.webdriver.support.wait import WebDriverWait

class Base():
    def __init__(self,driver):
        self.driver = driver
        """
                为什么使用find_element()方法去封装：
                    1. 元素定位方法底层用的全是 find_element()方法
                    2. 封装动态数据(ID,CLASS_NAME,XPATH)
                参数：
                    loc：为参数，数据类型为元组；*loc为解包
            """
    #查找单个元素
    def base_find_element(self,loc,timeout=30,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))
    #查找一组元素
    def base_find_elements(self,loc,timeout=30,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))

    #点击元素
    def base_click_element(self,loc):
        self.base_find_element(loc).click()
    #输入元素
    def base_input_element(self,loc,value):
        self.base_find_element(loc).clear()
        self.base_find_element(loc).sendkeys(value)




