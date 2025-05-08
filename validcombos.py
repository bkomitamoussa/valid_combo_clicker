from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def clicker(n, to_click):

    if to_click == 'yes':
        selector = 'div.radio:nth-child(1) > label:nth-child(1)'
    else: 
        selector = 'div.radio:nth-child(2) > label:nth-child(1)'   

    wait = WebDriverWait(browser, 20) 

    for i in range(n): 

        try:


            next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-primary.btn-go-to-next')))
            wait.until(lambda driver: next_button.is_enabled()) 

            sleep(1)

            radio_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
            radio_button.click()  

            next_button.click()  
            print(str(i+1) + ' clicks')
        
        except:
            print('Oh no, the clicker was not able to click!')

try:    
    browser = webdriver.Firefox()

    browser.get('https://gprl.surveycto.com/collect/main.html')

    response = input("Login and navigate to the valid combos section of the survey. Hit Enter to continue with the program when you are ready:").strip().lower()

    response = input("Enter 'yes' to click YES, enter 'no' to click NO:").strip().lower()
    if response == 'yes':
         click_choice = 'yes'
    if response == 'no':
         click_choice = 'no'
    print('you will be clicking: ' + click_choice)
    
    end_session = False
    while end_session==False:
        more_clicks = True
        while more_clicks==True:
              
            response = input("How many clicks? (enter an integer)").strip()
            number_of_clicks = int(response)

            clicker(n=number_of_clicks, to_click=click_choice)

            response = input("More clicks? (yes/no)").strip().lower()
            if response == 'yes':
                pass
            else: 
                 more_clicks = False

        response = input("End session? Make sure to save before ending: (yes/no)").strip().lower()
        if response == 'yes':
             end_session = True
        else: 
             pass
        
    print('shutting down...')
    browser.quit()

except Exception as e:
    print(str(e))
    print('shutting down...')
    browser.quit()
