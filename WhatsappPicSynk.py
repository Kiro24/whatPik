from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import time



contact = "Mark"
text = "hello from selenium"

def main():
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com")
    print("Please enter barcode")
    input()
    time.sleep(2)
    print("Logged In")

    inp_xpath_search = "//input[@title='Search or start new chat']"
    input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element_by_xpath(inp_xpath_search))
    input_box_search.click()
    time.sleep(2)
    input_box_search.send_keys(contact)
    time.sleep(2)

    selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
    selected_contact.click()

    inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
    input_box = driver.find_element_by_xpath(inp_xpath)
    time.sleep(2)
    #input_box.send_keys(text + Keys.ENTER)
    time.sleep(2)

    #Selecting profile pic element and downloading it 
    actions = ActionChains(driver)

    contact_info = driver.find_element_by_xpath('//*[@id="main"]/header/div[2]')
    contact_info.click()
    time.sleep(6)
    contact_img = driver.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/div[1]/div[1]/div[1]/div/img')
    #last session I figured out how to reach conatct prfile photo and click on the context menu but not able to save/copy it yet
    actions.context_click(contact_img).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.RETURN).perform()
    print("Saved img")
    time.sleep(5)


    driver.quit()

if __name__ == '__main__':
    main()