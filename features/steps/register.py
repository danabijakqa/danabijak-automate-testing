from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

@when('open danabijak page')
def homepage_register_up(context):
    context.driver.get('https://danabijak:sandboxdanabijak!123@sandbox.danabijak.com')

@then('user can access register page')
def click_register_button(context):
    context.driver.execute_script("window.scrollTo(0, 2000)")
    time.sleep(3)
    tk = context.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div/section[1]/div/div/div[2]/button')
    at = ActionChains(context.driver)
    at.click(on_element=tk).perform();
    time.sleep(3)    

@then('user input ktp')
def user_input_email(context):
    context.driver.execute_script("window.scrollTo(0, 200)")
    element = context.driver.find_element(By.NAME, 'personal_code_input')
    element.send_keys("3275062309932357") 
       

@then('user input phone number')
def user_input_telepon(context):
    element = context.driver.find_element(By.NAME, 'mobile_number')
    element.send_keys("85177990124")
          

@then('user input email register')
def user_input_email(context):
    element = context.driver.find_element(By.NAME, 'email')
    element.send_keys("ibnutest82@danabijak.com")
     

@then('user input password register')
def user_input_password(context):
    element = context.driver.find_element(By.XPATH, '//*[@id="password"]') 
    element.send_keys("123123")
    

@then('user input password confirmation')
def user_input__konfirmasi_password(context):
    element = context.driver.find_element(By.XPATH, '//*[@id="password_confirmation"]') 
    element.send_keys("123123")    
     

@then('user click checkbox syarat dan ketentuan') 
def user_click_checkbox(context):
    context.driver.execute_script("window.scrollTo(0, 200)")
    time.sleep(2)
    tk = context.driver.find_element(By.CLASS_NAME, "form-check-input")
    at = ActionChains(context.driver)
    at.click(on_element=tk).perform();
    time.sleep(2) 

@then('user click create account') 
def user_click_register_account(context):
    context.driver.execute_script("window.scrollTo(0, 300)")
    context.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div[2]/div/div/form/div[2]/div/button').click()
    time.sleep(5)  

    
    

