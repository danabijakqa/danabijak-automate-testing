from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Common Method

@given('open browser')
def open_browser(context):
    options = Options()
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    context.driver=webdriver.Chrome(chrome_options=options)    

@when('open danabijak site')
def homepage_show_up(context):
    context.driver.get('https://danabijak:sandboxdanabijak!123@sandbox.danabijak.com')

@then('close browser')
def close_browser(context):
    context.driver.close()

# Others Implementation

@then('user can see tkb90 info')
def see_tkb_info(context):
    context.driver.find_element(By.XPATH, '//*[@id="nav-collapse"]/ul/li[4]/button/span[2]')

@then('user can click login button')
def click_login_button(context):
    context.driver.find_element(By.XPATH, '//*[@id="main-calculator"]/div[1]/div/p[2]/a/u').click()

@then('user can click register button')
def click_register_button(context):
    context.driver.find_element(By.XPATH, '//*[@id="nav-collapse"]/ul/li[3]/button').click()
    time.sleep(3)

@then('user can click tentangkami page')
def click_tentangkami_button(context):
    context.driver.execute_script("window.scrollTo(0, 3000)")
    time.sleep(3)
    tk = context.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[4]/div/footer/div/div[1]/div[2]/h5/a')
    at = ActionChains(context.driver)
    at.click(on_element=tk).perform();
    time.sleep(7)

@then('user can click agendakegiatan page')
def click_tentangkami_button(context):
    context.driver.execute_script("window.scrollTo(0, 3000)")
    time.sleep(3)
    tk = context.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[4]/div/footer/div/div[1]/div[2]/ul/li[1]/a')
    at = ActionChains(context.driver)
    at.click(on_element=tk).perform();
    time.sleep(7) 

@then('user can click timkami page')
def click_timkami_button(context):
    context.driver.execute_script("window.scrollTo(0, 3000)")
    time.sleep(3)
    tk = context.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[4]/div/footer/div/div[1]/div[2]/ul/li[2]/a')
    at = ActionChains(context.driver)
    at.click(on_element=tk).perform();
    time.sleep(7)

@then('user can click pemberipinjaman page')
def click_pempinjaman_button(context):
    context.driver.execute_script("window.scrollTo(0, 3000)")
    time.sleep(3)
    tk = context.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[4]/div/footer/div/div[1]/div[2]/ul/li[3]/a')
    at = ActionChains(context.driver)
    at.click(on_element=tk).perform();
    time.sleep(7)    

@then('user can click faq page')
def click_faq_button(context):
    context.driver.execute_script("window.scrollTo(0, 3000)")
    time.sleep(3)
    tk = context.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[4]/div/footer/div/div[1]/div[3]/ul/li[1]/a')
    at = ActionChains(context.driver)
    at.click(on_element=tk).perform();
    time.sleep(7)     

@then('user can click carakerja page')
def click_carakerja_button(context):
    context.driver.execute_script("window.scrollTo(0, 3000)")
    time.sleep(3)
    tk = context.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[4]/div/footer/div/div[1]/div[3]/ul/li[2]/a')
    at = ActionChains(context.driver)
    at.click(on_element=tk).perform();
    time.sleep(7)    

@then('user can click informasibiaya page')
def click_infobiaya_button(context):
    context.driver.execute_script("window.scrollTo(0, 3000)")
    time.sleep(3)
    tk = context.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[4]/div/footer/div/div[1]/div[3]/ul/li[3]/a')
    at = ActionChains(context.driver)
    at.click(on_element=tk).perform();
    time.sleep(7)    

@then('user can click syaratketentuan page')
def click_syaratketentuan_button(context):
    context.driver.execute_script("window.scrollTo(0, 3000)")
    time.sleep(3)
    tk = context.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[4]/div/footer/div/div[1]/div[4]/ul/li[1]/a')
    at = ActionChains(context.driver)
    at.click(on_element=tk).perform();
    time.sleep(7)       

@then('user can click kebijakanprivasi page')
def click_kebijakan_button(context):
    context.driver.execute_script("window.scrollTo(0, 3000)")
    time.sleep(3)
    tk = context.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[4]/div/footer/div/div[1]/div[4]/ul/li[2]/a')
    at = ActionChains(context.driver)
    at.click(on_element=tk).perform();
    time.sleep(7)  

@then('user can click cekbiaya button')
def click_cekbiaya_button(context):
    context.driver.find_element(By.XPATH, '//*[@id="main-calculator"]/div[1]/div/button').click()

@then('user can click ajukanpinjaman page')
def click_ajukanpinjaman_button(context):
    context.driver.execute_script("window.scrollTo(0, 2000)")
    time.sleep(3)
    tk = context.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[2]/div/section[1]/div/div/div[2]/button')
    at = ActionChains(context.driver)
    at.click(on_element=tk).perform();
    time.sleep(10)      

@then('user can click playstore page') 
def click_playstore_button(context):
    context.driver.execute_script("window.scrollTo(0, 3000)")
    time.sleep(3)
    tk = context.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[4]/div/footer/div/div[1]/div[1]/a/img')
    at = ActionChains(context.driver)
    at.click(on_element=tk).perform();
    time.sleep(7)     

@then('user can click whatsapp number button')
def click_wanumber_button(context):
    context.driver.execute_script("window.scrollTo(0, 3000)")
    time.sleep(3)
    tk = context.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[4]/div/footer/div/div[2]/div[2]/ul/li[3]/a')
    at = ActionChains(context.driver)
    at.click(on_element=tk).perform();
    time.sleep(7)   

@then('user can click email button')
def click_email_button(context):
    context.driver.execute_script("window.scrollTo(0, 3000)")
    time.sleep(3)
    tk = context.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[4]/div/footer/div/div[2]/div[2]/ul/li[5]/a')
    at = ActionChains(context.driver)
    at.click(on_element=tk).perform();
    time.sleep(7)  

@then('user can click facebook button logo')
def click_facebook_button(context):
    context.driver.execute_script("window.scrollTo(0, 3000)")
    time.sleep(3)
    tk = context.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[4]/div/footer/div/div[2]/div[3]/ul/li[1]/a')
    at = ActionChains(context.driver)
    at.click(on_element=tk).perform();
    time.sleep(5)             

@then('user can click linkedin button logo')
def click_linkedin_button(context):
    context.driver.execute_script("window.scrollTo(0, 3000)")
    time.sleep(3)
    tk = context.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[4]/div/footer/div/div[2]/div[3]/ul/li[2]/a')
    at = ActionChains(context.driver)
    at.click(on_element=tk).perform();
    time.sleep(5)  

@then('user can click twitter button logo')
def click_twitter_button(context):
    context.driver.execute_script("window.scrollTo(0, 3000)")
    time.sleep(3)
    tk = context.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[4]/div/footer/div/div[2]/div[3]/ul/li[2]/a')
    at = ActionChains(context.driver)
    at.click(on_element=tk).perform();
    time.sleep(5)  

@then('user can click instagram button logo')
def click_instagram_button(context):
    context.driver.execute_script("window.scrollTo(0, 3000)")
    time.sleep(3)
    tk = context.driver.find_element(By.XPATH, '//*[@id="__layout"]/div/div[4]/div/footer/div/div[2]/div[3]/ul/li[4]/a')
    at = ActionChains(context.driver)
    at.click(on_element=tk).perform();
    time.sleep(5)    

#@then('user can click livechat casengo button')
#def click_cekbiaya_button(context):
 #   time.sleep(3)
  #  context.driver.find_element(By.XPATH, '//*[@id="casengo-inline-chat-status-button-text"]').click() 

@then('user can click keterangan persyaratan minimum button')
def click_keterangan_persyaratan_button(context):
    context.driver.execute_script("window.scrollTo(0, 200)")
    time.sleep(3)
    tk = context.driver.find_element(By.XPATH, '//*[@id="main-calculator"]/div[2]/button')
    at = ActionChains(context.driver)
    at.click(on_element=tk).perform();
    time.sleep(3)      
