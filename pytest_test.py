# -*- coding: utf-8 -*-
# @Time : 2024/3/18 11:06:13
# @Author : 小狂风
# File : pytest_test.py
# @Software : PyCharm

from utils import get_text_data, get_csv_data, get_excle_data
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


# 传统pytest.mark.parameter方法实现参数化，嵌套列表
@pytest.mark.parametrize(["username1", "password1"], [[456, 111], [123, 456], ["i", "o"], ["wa", "heihei"]])
def test_a(username1, password1):
    print(f"输入用户名:{username1}")  # f为字符串转义
    print(f"输入密码:{password1}")


# 调用utils包里面的get_text_data()封装方法
# 返回txt文档中的字符串参数化值：去掉\n换行符和空格，以,逗号进行分割
@pytest.mark.parametrize(["username2", "password2"], get_text_data())
def test_b(username2, password2):
    print(f"输入用户名:{username2}")
    print(f"输入密码:{password2}")


# 调用utils包里面的get_csv_data()封装方法
@pytest.mark.parametrize(["username3", "password3", "code3"], get_csv_data())
def test_c(username3, password3, code3):
    print(f"输入用户名:{username3}")
    print(f"输入密码:{password3}")
    print(f"输入验证码:{code3}")


# pytest实战：根据csv文档，实现参数化验证登录功能
@pytest.mark.parametrize(["username4", "password4", "code4"], get_csv_data())
def test_d(username4, password4, code4):
    driver = webdriver.Chrome()
    driver.get("http://192.168.5.213:5555/api-a/index")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.NAME, "loginId").send_keys(username4)
    driver.find_element(By.NAME, "pwd").send_keys(password4)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#loginform > div.__3wh-Hw9P.mt10 > input").click()
    driver.quit()


# pytest实战：根据excle文档，实现参数化验证登录功能
@pytest.mark.parametrize(["username5", "password5"], get_excle_data())
def test_e(username5, password5):
    driver = webdriver.Chrome()
    url = "http://192.168.5.135:5555/api-a/index"
    print("访问URL：" + url)
    driver.get(url)
    driver.maximize_window()
    time.sleep(1)

    # 输入用户名和密码
    print(f"输入用户名：{username5}")
    driver.find_element(By.NAME, "loginId").send_keys(username5)
    print(f"输入密码：{password5}")
    driver.find_element(By.NAME, "pwd").send_keys(password5)

    # 执行登录操作登录
    driver.find_element(By.CSS_SELECTOR, "#loginform > div.__3wh-Hw9P.mt10 > input").click()

    try:
        # 登录限制，是否弹窗
        alert_button = driver.find_element(By.XPATH, "//button[text()='确定']")

        # 判断弹窗按钮是否存在，存在则进行点击，不存在则继续后续动作
        if alert_button.is_displayed():
            print("弹出登录限制窗，点击确认强制登录")
            time.sleep(1)
            alert_button.click()
            time.sleep(1)
        else:
            time.sleep(1)
            print("未弹出登录限制框，继续执行后续步骤")
    except NoSuchElementException:
        print("未找到元素")

    # alert_button = driver.find_element(By.XPATH, "//button[text()='确定']")
    # if alert_button.is_displayed():
    #     print("存在登录限制弹窗按钮，需点击确定进行强制登录")
    #     time.sleep(1)
    #     alert_button.click()
    # else:
    #     print("元素不存在，正常执行")

    # 等待你好元素信息呈现
    WebDriverWait(driver, 5).until(
        EC.invisibility_of_element_located((By.XPATH, "//div[contains(text(),'你好')]"))
    )
    # 断言title是否正确
    assert driver.title == "联通物联网数字化运营平台"
    print("判断标题：" + driver.title + "，是否为：联通物联网数字化运营平台")
    time.sleep(1)

    driver.find_element(By.XPATH, "//input[@id='search_lst']").send_keys("N1N2统计分析")
    time.sleep(1)

    driver.find_element(By.XPATH, "//span[@class='aa-suggestions']//div[@class='aa-suggestion']").click()
    print("点击进入搜索框下拉菜单中的模块")
    time.sleep(1)

    driver.switch_to.frame(1)
    print("切换iframe")
    time.sleep(1)

    driver.find_element(By.XPATH, "//div[@id='queryid']").click()
    print("执行查询操作")
    time.sleep(1)

    print("默认120秒，等待元素消失")
    WebDriverWait(driver, 120).until(
        EC.invisibility_of_element_located((By.XPATH, "//div[contains(@class,'mask-spinner')]"))
    )

    driver.quit()
