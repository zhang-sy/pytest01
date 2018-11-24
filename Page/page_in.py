from Base.get_driver import get_driver
from Page.page_login import PageLogin
from Page.page_setting import PageSetting

driver = get_driver()
class PageIn():
    # 获取登录页面对象
    def page_get_login(self):
        return PageLogin(driver)
    # 获取设置页面对象
    def page_get_setting(self):
        return PageSetting(driver)


