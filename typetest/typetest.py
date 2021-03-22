from selenium import webdriver
from selenium.webdriver.common.keys import Keys
path = "chromedriver.exe"

driver = webdriver.Chrome(path)

driver.get("https://www.livechat.com/typing-speed-test/#/")


def result():
    wpm = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/span/div/div/div/div/div[2]/div/div[2]/p/span[3]/span[1]')
    return wpm

def something():
    a = input("1 : 타자연습 시작\n2 : 빠른모드\n3 : 종료입력: ")
    while True:
        if a == "1":

            while True:
                try:
                    result()
                    print("결과가 나왔습니다")
                except:
                    word = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/span/div[2]/span/div/div[2]/div[2]/span[1]').text
                    print(word)
                    for i in word:
                        driver.find_element_by_xpath('//*[@id="test-input"]').send_keys(i)
                    driver.find_element_by_xpath('//*[@id="test-input"]').send_keys(Keys.SPACE)

        elif a == "2":

            while True:
                try:
                    result()
                    print("결과가 나왔습니다")
                except:
                    word = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[1]/div/span/div[2]/span/div/div[2]/div[2]/span[1]').text
                    print(word)
                    driver.find_element_by_xpath('//*[@id="test-input"]').send_keys(word)
                    driver.find_element_by_xpath('//*[@id="test-input"]').send_keys(Keys.SPACE)

        else:

            print("ㅂㅂㅂㅂㅂ")
            break

something()

