# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import config

browser = webdriver.Chrome()


# 攻击方用户登录系统
def test_login1():
    browser.get(config.remotehost)
    time.sleep(1)
    username = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/input')
    username.clear()
    username.send_keys('cs_attacker')  # 输入用户名
    time.sleep(1)
    password = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/input')
    password.clear()
    password.send_keys('admin123')  # 输入密码
    time.sleep(1)
    ver = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[3]/div/div/input')
    password.clear()
    ver.send_keys('x')  # 输入验证码
    time.sleep(1)
    login = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[4]/div/button')
    login.click()
    time.sleep(1)
    assert 0 == 0


def test_chang1():
    browser.get(config.remotehost + "/#/page/notice")
    time.sleep(1)
    newpa = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/form/div[3]/div/div/input')
    newpa.send_keys('Admin123')
    time.sleep(1)  # 输入新密码
    nerpa = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/form/div[4]/div/div[1]/input')
    nerpa.send_keys('Admin123')
    time.sleep(1)  # 确认密码
    old = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/form/div[5]/div/div[1]/input')
    old.send_keys('admin123')
    time.sleep(1)  # 旧密码
    ve = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]/span')
    ve.click()
    time.sleep(1)
    assert 0 == 0


def test_login2():
    # 用户名 密码
    browser.get(config.remotehost)
    time.sleep(1)
    username = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/input')
    username.clear()
    username.send_keys('cs_victim')  # 输入用户名
    time.sleep(1)
    password = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/input')
    password.clear()
    password.send_keys('admin123')  # 输入密码
    time.sleep(1)
    ver = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[3]/div/div/input')
    password.clear()
    ver.send_keys('x')  # 输入验证码
    time.sleep(1)
    login = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[4]/div/button')
    login.click()
    time.sleep(1)
    assert 0 == 0


def test_chang2():
    browser.get(config.remotehost + "#/page/notice")
    time.sleep(1)
    newpa = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/form/div[3]/div/div/input')
    newpa.send_keys('Admin123')
    time.sleep(1)  # 输入新密码
    nerpa = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/form/div[4]/div/div[1]/input')
    nerpa.send_keys('Admin123')
    time.sleep(1)  # 确认密码
    old = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/form/div[5]/div/div[1]/input')
    old.send_keys('admin123')
    time.sleep(1)  # 旧密码
    ve = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]/span')
    ve.click()
    time.sleep(1)
    assert 0 == 0


def test_login3():
    # 用户名 密码
    browser.get(config.remotehost)
    time.sleep(1)
    username = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/input')
    username.clear()
    username.send_keys('cs_judge1')  # 输入用户名
    time.sleep(1)
    password = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/input')
    password.clear()
    password.send_keys('admin123')  # 输入密码
    time.sleep(1)
    ver = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[3]/div/div/input')
    password.clear()
    ver.send_keys('x')  # 输入验证码
    time.sleep(1)
    login = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[4]/div/button')
    login.click()
    time.sleep(1)
    assert 0 == 0


def test_chang3():
    browser.get(config.remotehost + "/#/page/notice")
    time.sleep(1)
    newpa = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/form/div[3]/div/div/input')
    newpa.send_keys('Admin123')
    time.sleep(1)  # 输入新密码
    nerpa = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/form/div[4]/div/div[1]/input')
    nerpa.send_keys('Admin123')
    time.sleep(1)  # 确认密码
    old = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/form/div[5]/div/div[1]/input')
    old.send_keys('admin123')
    time.sleep(1)  # 旧密码
    ve = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]/span')
    ve.click()
    time.sleep(1)
    assert 0 == 0


def test_login4():
    # 用户名 密码
    browser.get(config.remotehost)
    time.sleep(1)
    username = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/input')
    username.clear()
    username.send_keys('cs_judge2')  # 输入用户名
    time.sleep(1)
    password = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/input')
    password.clear()
    password.send_keys('admin123')  # 输入密码
    time.sleep(1)
    ver = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[3]/div/div/input')
    password.clear()
    ver.send_keys('x')  # 输入验证码
    time.sleep(1)
    login = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[4]/div/button')
    login.click()
    time.sleep(1)
    assert 0 == 0


def test_chang4():
    browser.get(config.remotehost + "/#/page/notice")
    time.sleep(1)
    newpa = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/form/div[3]/div/div/input')
    newpa.send_keys('Admin123')
    time.sleep(1)  # 输入新密码
    nerpa = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/form/div[4]/div/div[1]/input')
    nerpa.send_keys('Admin123')
    time.sleep(1)  # 确认密码
    old = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/form/div[5]/div/div[1]/input')
    old.send_keys('admin123')
    time.sleep(1)  # 旧密码
    ve = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]/span')
    ve.click()
    time.sleep(1)
    assert 0 == 0


def test_login5():
    # 用户名 密码
    browser.get(config.remotehost)
    time.sleep(1)
    username = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[1]/div/div[1]/input')
    username.clear()
    username.send_keys('cs_expert')  # 输入用户名
    time.sleep(1)
    password = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div/input')
    password.clear()
    password.send_keys('admin123')  # 输入密码
    time.sleep(1)
    ver = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[3]/div/div/input')
    password.clear()
    ver.send_keys('x')  # 输入验证码
    time.sleep(1)
    login = browser.find_element_by_xpath('/html/body/div[1]/div/div/form/div[4]/div/button')
    login.click()
    time.sleep(1)
    assert 0 == 0


def test_chang5():
    browser.get(config.remotehost + "/#/page/notice")
    time.sleep(1)
    newpa = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/form/div[3]/div/div/input')
    newpa.send_keys('Admin123')
    time.sleep(1)  # 输入新密码
    nerpa = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/form/div[4]/div/div[1]/input')
    nerpa.send_keys('Admin123')
    time.sleep(1)  # 确认密码
    old = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/form/div[5]/div/div[1]/input')
    old.send_keys('admin123')
    time.sleep(1)  # 旧密码
    ve = browser.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/button[2]/span')
    ve.click()
    time.sleep(1)
    assert 0 == 0
    browser.close()
