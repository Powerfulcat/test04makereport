# 需求：
#     1. iweb项目登陆，输入正确用户名和密码，断言登录成功的用户名是否为admin，
#     如果断言失败截图保存；
#
# 扩展：
#     1. 图片名称为动态-时间
#     2. 图片名称添加断言错误信息

import unittest
from selenium import webdriver
from time import sleep
# 导入时间包
import time
# 导入sys
import sys


class IWebShop(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        # url = 'http://172.16.200.157/iwebshop/'
        url = 'http://localhost:8080/iwebshop/'
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        driver = self.driver
        sleep(3)
        driver.quit()

    def test_login_in(self):
        # 元素定位及操作
        driver = self.driver
        # 点击 登录
        driver.find_element_by_link_text('登录').click()
        # 输入账号及密码
        driver.find_element_by_css_selector("[name='login_info']").send_keys('test')
        driver.find_element_by_css_selector("[name='password']").send_keys('123456')
        # 点击登录按钮
        driver.find_element_by_class_name('submit_login').click()

        try:
            # 获取登录后的信息
            result = driver.find_element_by_class_name('loginfo').text
            # print(result)
            self.assertIn('admin', result)
        except AssertionError:
            # 获取当前时间
            '''
            Y:年,m:月,d:日 H:小时,M:分钟,S:秒
            '''
            now_time = time.strftime('%Y-%m-%d %H_%M_%S')
            # 获取异常信息
            exc_info = sys.exc_info()
            # print(type(exc_info))
            # print(exc_info)
            driver.get_screenshot_as_file('./Images/%s-%s.png' % (now_time, exc_info[1]))
            raise


if __name__ == '__main__':
    unittest.main()
