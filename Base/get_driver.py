from appium import webdriver
def get_driver():
    # server 启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '6.0.1'
    desired_caps['deviceName'] = '127.0.0.1:7555'
    # app信息
    desired_caps['appPackage'] = 'com.android.settings'
    desired_caps['appActivity'] = '.Settings'

    return webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


