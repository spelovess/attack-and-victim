
# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import config

browser = webdriver.Chrome()


# 攻击方用户登录系统
def test_login():
    # 用户名 密码
    browser.get(config.remotehost)
    time.sleep(1)
    username = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/input')
    username.clear()
    username.send_keys('cs_expert')  # 输入用户名
    time.sleep(1)
    password = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/input')
    password.clear()
    password.send_keys('Admin123')  # 输入密码
    time.sleep(1)
    ver = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[3]/div/div/input')
    password.clear()
    ver.send_keys('x')  # 输入验证码
    time.sleep(1)
    login = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[4]/div/button')
    login.click()
    time.sleep(1)
    assert 0 == 0


def test_df():
    browser.get(config.remotehost + '/#/page/score/highRisk')
    time.sleep(5)
    look = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[1]/div[2]/div[1]/div[3]/table/tbody/t'
        'r[1]/td[9]/div/button[1]/span')
    look.click()
    time.sleep(1)  # 点击查看
    sq = browser.find_element_by_xpath('//*[@id="app"]/section/section/main/div/div[2]/div[3]/'
                                       'div[1]/p/button/span')
    sq.click()
    time.sleep(1)  # 点击审核申请
    pass1 = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[2]/div[4]/div/div/div[2]/form/div[1]'
        '/div/div/label[1]/span[1]/span')
    pass1.click()
    time.sleep(1)  # 点击通过
    comm = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[2]/div[4]/div/div/div[2]/form/div[2]/'
        'div/div[1]/textarea')
    comm.send_keys('comments')
    time.sleep(1)  # 输入评论意见
    ver = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[2]/div[4]/div/div/div[3]/div/button[1]/span')
    ver.click()
    time.sleep(1)  # 点击确定
    back = browser.find_element_by_xpath('//*[@id="app"]/section/section/main/div/div[2]/'
                                         'div[1]/button/span/span')
    back.click()
    time.sleep(1)  # 点击返回列表
    assert 0 == 0


def test_df1():
    browser.get(config.remotehost + '/#/page/score/highRisk')
    time.sleep(5)
    look = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[1]/div[2]/div[1]/div[3]/table/tbody/tr[2'
        ']/td[9]/div/button[1]/span')
    look.click()
    time.sleep(1)  # 点击查看
    sq = browser.find_element_by_xpath('//*[@id="app"]/section/section/main/div/div[2]/div[3]/div'
                                       '[1]/p/button/span')
    sq.click()
    time.sleep(1)  # 点击审核申请
    pass1 = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[2]/div[4]/div/div/div[2]/form/div[1]/di'
        'v/div/label[2]/span[2]')
    pass1.click()
    time.sleep(1)  # 点击驳回
    comm = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[2]/div[4]/div/div/div[2]/form/div[2]/di'
        'v/div[1]/textarea')
    comm.send_keys('comments')
    time.sleep(1)  # 输入评论意见
    ver = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[2]/div[4]/div/div/div[3]/div/button[1]/span')
    ver.click()
    time.sleep(1)  # 点击确定
    back = browser.find_element_by_xpath('//*[@id="app"]/section/section/main/div/div[2]/div'
                                         '[1]/button/span/span')
    back.click()
    time.sleep(1)  # 点击返回列表
    assert 0 == 0
    browser.close()
