import pytest
import os,sys
sys.path.append(os.getcwd())
from Page.page_in import PageIn

class TestSetting():
    def setup_class(self):
# 实例化统一入口类
        self.setting = PageIn().page_get_setting()

    def teardown_class(self):
        self.setting.driver.quit()
    #测试方法
    @pytest.mark.parametrize("value,except_result",[("l","移动网络"),("a","壁纸"),("w","wlan")])
    def test_setting(self,except_result,value='wlan'):
        #点击搜索按钮
        self.setting.page_click_search_btn()
        #输入
        self.setting.page_input_search(value)
        #断言
        try:
            #获取当前搜索结果的列表
            list_text = self.setting.page_get_elements()
            assert except_result in list_text
            print("获取的列表文本为",list_text)
            print("断言成功")
        except:
            print('断言失败')

        #点击返回
        self.setting.page_click_back()