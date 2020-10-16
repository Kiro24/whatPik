from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
# chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")
# assert "Python" in driver.title
driver.save_screenshot("image.png")
if "Python" in driver.title:
    print("Python")
# elem = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/header/div[1]/div/img')
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# print(elem)
driver.close()