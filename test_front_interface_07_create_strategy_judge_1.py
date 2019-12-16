# -*- coding: utf-8 -*-

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import time
import config

browser = webdriver.Chrome()


def test_login():
    browser.get(config.remotehost)
    time.sleep(1)
    username = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/input')
    username.clear()
    username.send_keys('admin')  # 输入用户名
    time.sleep(1)
    password = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/input')
    password.clear()
    password.send_keys('admin')  # 输入密码
    time.sleep(1)
    ver = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[3]/div/div/input')
    password.clear()
    ver.send_keys('x')  # 输入验证码
    time.sleep(1)
    login = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[4]/div/button')
    login.click()
    time.sleep(1)
    assert 0 == 0


def test_setpz():
    browser.get(config.remotehost + '/#/page/plat/systemSetting')
    time.sleep(1)
    sl = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div/div/div/div/div[2]/di'
        'v[1]/div/div/div/div/form/div[4]/div/div/input')
    ActionChains(browser).double_click(sl).perform()
    sl.send_keys(2)
    time.sleep(1)
    veri = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div/div/div/div/div[2]/div[1]/div'
        '/div/div/div/div/button[1]/span')
    veri.click()
    time.sleep(1)
    veri2 = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div[3]/button[1]/span')
    veri2.click()
    time.sleep(1)
    advance = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div/div/div/div/div[1]/div/div/div/div[1]/div[3]/div')
    advance.click()
    time.sleep(1)  # 点击演习高级设置
    reset = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div/div/div/div/div[2]/div[2]/div/div/'
        'div/div/div/button[2]/span')
    reset.click()
    time.sleep(1)  # 点击重置按钮
    ver = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/div[3]/button[1]/span')
    ver.click()
    time.sleep(1)  # 重置的确认
    butt = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div/div/div/div/div[2]/div[2]/div/d'
        'iv/div/div/form/div[2]/div/div/span/span[2]')
    butt.click()
    time.sleep(1)  # 点击决策裁判数的开关
    ve = butt.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div/div/div/div/div[2]/di'
        'v[2]/div/div/div/div/div/button[1]/span')
    ve.click()
    time.sleep(1)  # 点击确定
    ve2 = browser.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div/div[3]/button[1]/span')
    ve2.click()
    time.sleep(1)  # 点击二次确定
    assert 0 == 0


def test_create_strategy():
    browser.get(config.remotehost + '/#/page/strategy')
    time.sleep(1)
    add = browser.find_element_by_xpath('//*[@id="app"]/section/section/main/div/div[1]/'
                                        'div[2]/button[1]/span')
    add.click()
    time.sleep(5)  # 点击添加按钮
    sname = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[3]/div/div/div[2]/form/div[1]/div/div[1]/input')
    sname.send_keys("策略一")
    time.sleep(1)  # 填写策略名称
    gx = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[3]/div/div/div[2]/form/div[2]/div/'
        'div/div[1]/div/div[2]/label/span[1]/span')
    gx.click()
    time.sleep(1)  # 勾选攻击队伍前面的复选框
    jt = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[3]/div/div/div[2]/form/div[2]/div/'
        'div/div[2]/button[2]/span/i')
    jt.click()
    time.sleep(1)  # 点击箭头转向
    fs = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[3]/div/div/div[2]/form/div[3]/d'
        'iv/div/div[1]/div/div[2]/label/span[1]/span')
    fs.click()
    time.sleep(1)  # 点击防守队伍前面的复选框
    jt1 = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[3]/div/div/div[2]/form/div[3]/d'
        'iv/div/div[2]/button[2]/span/i')
    jt1.click()
    time.sleep(1)  # 点击箭头转向
    cp = browser.find_element_by_xpath(
        '/html/body/div[1]/section/section/main/div/div[3]/div/div/div[2]/form/div[4]/di'
        'v/div/div[1]/div/div[2]/label[1]/span[1]/span')
    cp.click()
    time.sleep(1)  # 选择一个裁判
    jt2 = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[3]/div/div/div[2]/form/div[4]/div'
        '/div/div[2]/button[2]/span/i')
    jt2.click()
    time.sleep(1)  # 点击箭头转向
    bz = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[3]/div/div/div[2]/form/div[5]/div/div/textarea')
    bz.send_keys("备注内容")
    time.sleep(1)  # 输入备注
    num = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[3]/div/div/div[2]/form/div[6]/div/div[1]/input')
    num.send_keys(2)
    time.sleep(1)  # 输入决策裁判数
    veri = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[3]/div/div/div[2]/form/div[8]/button[1]/span')
    veri.click()
    time.sleep(1)  # 点击确认
    assert 0 == 0
    browser.close()
