from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 
from pathlib import Path
import time 
import random 
import copy  
import pandas as pd  
import os 
from openpyxl import workbook 
import csv


class Browser_Launch:
    def __init__(self):
        self.brave_path=f"C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
        self.driver_path=f"Requirements/WEB-DRIVERS/chromedriver.exe"
        self.service = Service(executable_path=self.driver_path)
    def browser_launch_opts(self):
        options = webdriver.ChromeOptions()
        options = Options()
        options.add_experimental_option("detach", True)
        options.binary_location = self.brave_path
        self.driver = webdriver.Chrome(service=self.service,options=options)
        self.driver.get("https://www.instagram.com/")

    def login(self):
        self.username = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']")))
        self.username.send_keys("mstsdev963")
        self.password = self.driver.find_element(By.XPATH, "//input[@name='password']")
        self.password.send_keys("WBE963633")
        self.login = self.driver.find_element(By.XPATH,"//*[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']",)
        self.login.click()
    def read_users(self): 
        self.file_path=f"Requirements/archive/users.txt"
        self.file=open(self.file_path,"r") 
        self.read=self.file.readlines() 
        self.users_list=[] 
        for self.line in self.read:
            if self.line[-1]=='\n': 
                self.users_list.append(self.line[:-1]) 
        # print(*([""]+self.new_list),sep='\n')
        # print("\n",self.new_list,sep="\n")

    def get_data(self): 
        delay=random.uniform(3,6) 
        time.sleep(delay) 
        self.store = {}  
        self.store_value=[]
        for self.i in self.users_list: 
            self.user=self.i
            self.driver.get(f"https://www.instagram.com/{self.user}")  
            delay=random.uniform(3,6) 
            time.sleep(delay)  
            self.ul = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//ul[@class='x78zum5 x1q0g3np xieb3on']"))) 
            self.items=self.ul.find_elements("xpath","//li[@class='xl565be x1m39q7l x1uw6ca5 x2pgyrj']")   
            self.image = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='_aagv']"))) 
            self.alt=self.image.find_element(By.TAG_NAME,'img').get_attribute('alt')
            delay=random.uniform(3,6) 
            time.sleep(delay) 
            print(self.alt)
            self.key = self.user
            for self.j in self.items:
                self.store_value.append(self.j.text) 
                self.store.update({self.key:copy.deepcopy(self.store_value)}) 
            self.store_value.clear() 
        print(self.store)

    def save_to_excel(self):  
        self.folder_name="STORED DATA" 
        self.file_name="output.xlsx"
        if not os.path.exists(self.folder_name): 
            os.makedirs(self.folder_name)
        self.workbook=workbook.Workbook() 
        self.sheet=self.workbook.active
        self.sheet
        self.sheet["A1"]="Users"
        self.sheet["B1"]="Data"
        
        for self.k,self.l,self.m in enumerate(self.store.items(),start=2):
            self.sheet[f"A{self.k}"]=self.l 
            self.sheet[f"B{self.k}"]=self.m 
            
        self.workbook.save("{self.folder_name}/{self.file_name}")
        
        


browser = Browser_Launch()
browser.browser_launch_opts()
# browser.login()
browser.read_users()
browser.get_data() 
browser.save_to_excel()
