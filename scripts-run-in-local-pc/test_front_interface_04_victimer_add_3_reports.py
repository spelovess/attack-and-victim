# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import os
import config

browser = webdriver.Chrome()


# 攻击方用户登录系统
def test_login():
    # 用户名 密码
    time.sleep(1)
    browser.get(config.remotehost)
    time.sleep(1)
    username = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/input')
    username.clear()
    username.send_keys('cs_victim')  # 输入用户名
    time.sleep(1)
    password = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/input')
    password.clear()
    password.send_keys('Admin123')  # 输入密码
    time.sleep(1)
    ver = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[3]/div/div/input')
    password.clear()
    ver.send_keys('sf')  # 输入验证码
    time.sleep(1)
    login = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[4]/div/button')
    login.click()
    time.sleep(1)
    assert 0 == 0


def test_victim_submit_grade():
    time.sleep(1)
    # 防守单位第几个，目标IP，目标系统，url，攻击类型第几个，说明，成绩图片，文件
    browser.get(config.remotehost + '/#/page/score')
    time.sleep(1)
    submit_grade = browser.find_element_by_xpath('//*[@id="app"]/section/secti'
                                                 'on/main/div/div[1]/div[2]/button[1]/span')
    submit_grade.click()  # 点击提交成绩
    time.sleep(1)
    MBSYSTEM = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[3]/div/div/div[2]/form/div[1]/div/div[1]/input')
    MBSYSTEM.send_keys('系统一')
    time.sleep(1)  # 输入目标系统
    MBIP = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[3]/div/div/div[2]/form/div[2]/div/div[1]/input')
    MBIP.send_keys('1.1.1.1')
    time.sleep(1)  # 输入目标IP
    MBURL = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[3]/div/div/div[2]/form/div[3]/div/div[1]/input')
    MBURL.send_keys('http://adsf.asdf.asdf')
    time.sleep(1)  # 输入目标URL
    GJCKIP = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[3]/div/div/div[2]/form/div[4]/div/div[1]/input')
    GJCKIP.send_keys('12.12.12.12')
    time.sleep(1)  # 输入攻击出口IP
    GJSD = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[3]/div/div/div[2]/form/div[5]/div/div[1]/textarea')
    GJSD.send_keys('SQL注入')  # 输入攻击手段
    time.sleep(1)
    FYSD1 = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[3]/div/div/div[2]/form/div[6]/div/div[1]/div[1]/p/i')
    FYSD1.click()
    time.sleep(1)  # 点击下拉框
    FYSD2 = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[3]/div/div/div[2]/form/div[6]'
        '/div/div[1]/div[2]/div[1]/span[1]/label/span[1]/span')
    FYSD2.click()
    time.sleep(1)  # 勾选前面的勾勾
    FYSD3 = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[3]/div/div/div[2]/form/div[6]/div/div'
        '[1]/div[2]/div[1]/span[2]/div/input')
    FYSD3.send_keys(2)
    time.sleep(1)  # 输入数量
    CGSM = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[3]/div/div/div[2]/form/div[7]/div/div[1]/textarea')
    CGSM.send_keys('防守成功')
    time.sleep(1)  # 输入成果说明
    Image = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[3]/div/div/div[2]/form/div[8]/div/div/label/input')
    Image.send_keys(os.path.abspath('pic1.png'))
    time.sleep(1)
    documents = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[3]/div/div/div[2]/form/div[9]/div/button/span')
    documents.click()
    time.sleep(1)
    documents = browser.find_element_by_xpath('//*[@id="fileUpload"]/div[1]/input')
    documents.send_keys(os.path.abspath('攻击方成果报告.docx'))
    time.sleep(1)
    confirm = browser.find_element_by_xpath(
        '//*[@id="app"]/section/section/main/div/div[3]/div/div/div[2]/div/button[1]/span')
    confirm.click()
    time.sleep(1)
    assert 0 == 0
    browser.close()
