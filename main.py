import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from config import *
import random
import logging

import selenium_metamask_automation

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s", filename="log.log",filemode="w")

lis=[]


tx=0


with open("wallet.txt", "r") as f:

    text=f.read().strip()
    t=text.split("\n")

    for i in range(len(t)):
            lis.append(t[i].split(", "))


for i in range(len(lis)):

    

    driver = selenium_metamask_automation.launchSeleniumWebdriver('F:\project\chromedriver.exe')




    driver.switch_to.window(driver.window_handles[1])






    sleep(1)

    
    driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/create-password/import-with-seed-phrase")


    inp1=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/form/div[4]/div[1]/div/input').send_keys(lis[i][0])

    inp2=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/form/div[5]/div/input').send_keys("wewewewe")

    inp3=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/form/div[6]/div/input').send_keys("wewewewe")

    inp5=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/form/button')


    driver.execute_script("arguments[0].removeAttribute('disabled')", inp5)

    sleep(1)

    inp4=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div/form/div[7]/div').submit()

    sleep(3)

    driver.maximize_window()

    

    sleep(3)



    driver.get("https://app.zerion.io/connect-wallet")



    sleep(4)

    inp8=driver.find_element(By.XPATH, '//*[@id="PageWrapper"]/div/div/div[2]/div[2]/div/div[1]/div/div/button[2]').click()






    sleep(2)

    driver.switch_to.window(driver.window_handles[2])

    sleep(1)



    inp9=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div[4]/div[2]/button[2]')
    driver.execute_script('arguments[0].click()', inp9)

    inp10=driver.find_element(By.XPATH, '/html/body/div[1]/div/div[3]/div/div[2]/div[2]/div[2]/footer/button[2]')
    driver.execute_script('arguments[0].click()', inp10)

    driver.switch_to.window(driver.window_handles[1])


    


    sleep(3)

    driver.get("https://app.zerion.io/send/token")

    sleep(2)

    inp11=driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/div[3]/div/div/div[3]/div/div/form/div[1]/button')
    driver.execute_script('arguments[0].click()', inp11)

    sleep(2)

    inp12=driver.find_element(By.XPATH, '/html/body/div[1]/div[5]/div/div[3]/div/div/div[3]/div/div/form/div[1]/div[1]/div/button[7]')
    driver.execute_script('arguments[0].click()', inp12)

    sleep(1)

    for a in range(txa):
        try:
            
            inp14=driver.find_element(By.XPATH, '//*[@id="buy"]')

            inp14.send_keys(str(round((random.uniform(min_xdai, max_xdai)), 5)))

            sleep(2)


            inp13=driver.find_element(By.XPATH, '//*[@id="send-to"]').send_keys(lis[i][1])

            sleep(4)



            inp17=driver.find_element(By.XPATH, '//*[@id="PageWrapper"]/div/div[3]/div/div/form/button')
            driver.execute_script('arguments[0].click()', inp17)

            sleep(4)

            driver.switch_to.window(driver.window_handles[2])

            sleep(4)
            if a==0:
                mm1=driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/button[2]')
                driver.execute_script('arguments[0].click()', mm1)

                sleep(1)

                mm2=driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/button[2]')
                driver.execute_script('arguments[0].click()', mm2)

                sleep(5)

                driver.switch_to.window(driver.window_handles[2])

            sleep(1)

            inp18=driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[3]/div[3]/footer/button[2]')
            driver.execute_script('arguments[0].click()', inp18)



            driver.switch_to.window(driver.window_handles[1])

            sleep(5)

            inp18=driver.find_element(By.XPATH, '//*[@id="PageWrapper"]/div/div[3]/div/div[1]/div/div[3]/div[3]/button')
            driver.execute_script('arguments[0].click()', inp18)

            tx+=1

            

            sleep(random.randint(tx_pause_min, tx_pause_max))
            
        except:
            
            pass

            



    
    
    logging.info(f"Wallet {lis[i][1]}| Success {tx}")
    tx=0

    driver.quit()

    

    sleep(1)































#C:\Users\1\AppData\Local\Google\Chrome\User Data\Default\Extensions\acmacodkjbdgmoleebolmdjonilkdbch\acmacodkjbdgmoleebolmdjonilkdbch.pem








