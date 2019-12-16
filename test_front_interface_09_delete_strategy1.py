# -*- coding: utf-8 -*-

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


def test_delete_strategy():
    browser.get(config.remotehost + '/#/page/strategy')
    time.sleep(1)
    fxk = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[2]/div[1]/div[2]/table'
        '/thead/tr/th[2]/div/label/span/span')
    fxk.click()
    time.sleep(1)  # 勾选全选复选框
    plsc = browser.find_element_by_xpath('//*[@id="app"]/section/section/main/div/'
                                         'div[1]/div[2]/button[2]/span')
    plsc.click()
    time.sleep(1)  # 点击批量删除
    ve = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div[3]/button[1]/span')
    ve.click()
    time.sleep(1)  # 点击确认
    assert 0 == 0
    browser.close()
