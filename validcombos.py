from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def fast_click_next(browser):

    header_text = browser.find_element(By.CSS_SELECTOR, "#go-to-prompt-control-title").text
    # print(header_text)
    browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary.btn-go-to-next').click()
    WebDriverWait(browser, 300).until(
        lambda driver: driver.find_element(By.CSS_SELECTOR, "#go-to-prompt-control-title").text != header_text
    )
    WebDriverWait(browser, 300).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#frame-nav-next'))
    )
    WebDriverWait(browser, 300).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".label-container"))
    )

def pattern_clicker(n, pattern, browser_object):

    wait = WebDriverWait(browser_object, 20) 

    for i in range(n):
        for letter in pattern:
            if letter == 'y':
                selector = 'div.radio:nth-child(1) > label:nth-child(1)'
            if letter == 'n':
                selector = 'div.radio:nth-child(2) > label:nth-child(1)'   
            
            try:

                radio_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
                radio_button.click()  

                fast_click_next(browser_object)
                print('pattern ' + str(i+1) + ', ' + ' click ' + letter)

                sleep(0.75)
        
            except:
                print('Oh no, the clicker was not able to click!')
            
def clicker(n, to_click, browser_object):

    if to_click == 'yes':
        selector = 'div.radio:nth-child(1) > label:nth-child(1)'
    else: 
        selector = 'div.radio:nth-child(2) > label:nth-child(1)'   

    wait = WebDriverWait(browser_object, 20) 

    for i in range(n): 

        try:

            radio_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
            radio_button.click()  

            fast_click_next(browser_object)
            print(str(i+1) + ' clicks')

            sleep(0.75)
        
        except:
            print('Oh no, the clicker was not able to click!')

try:    
    browser = webdriver.Firefox()

    browser.get('https://gprl.surveycto.com/collect/main.html')

    print('email: bkomitamoussa@uchicago.edu')
    print('password: p&cZA5g,&mN+7U;')


    response = input("Login and navigate to the valid combos section of the survey. Hit Enter to continue with the program when you are ready:").strip().lower()


    
    end_session = False
    while end_session==False:

        click_pattern = input("Enter click pattern as string of ys and ns, e.g. 'ynyn':").strip().lower()
        '''
        if response == 'yes':
            click_choice = 'yes'
        if response == 'no':
            click_choice = 'no'
        '''
        print('you will be clicking: ' + click_pattern)

        more_clicks = True
        while more_clicks==True:
              
            response = input("How many pattern repititions? (enter an integer)").strip()
            number_of_patterns = int(response)


            pattern_clicker(n = number_of_patterns, pattern=click_pattern, browser_object=browser)
            #clicker(n=number_of_clicks, to_click=click_choice, browser_object=browser)

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
