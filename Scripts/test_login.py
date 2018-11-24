import os,sys

import allure
import pytest

sys.path.append(os.getcwd())
from Page.page_in import PageIn

class TestLogin():
    @allure.step('执行登录操作')
    #初始化
    def setup_class(self):
    #实例化PageLogin
        self.login = PageIn().page_get_login()
    @allure.step('退出')
    def teardown_class(self):
        self.login.driver.quit()
        """
         def page_param_data(self):
        arrs=[]
        yaml_data =
        #没写完
            @pytest.mark.parametrize('username,password,expect_toast',[])

        """


    def test_login(self,value1,value2):
        allure.attach('输入用户名')
        #输入用户名
        self.login.page_input_usename(value1)
        allure.attach('输入密码')
        #输入密码

        self.login.page_input_pwd(value2)
        #点击的登陆陆
        self.login.page_click_log_btn()





