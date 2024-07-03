from selenium import webdriver

def getDriver():
  options = webdriver.ChromeOptions()
  options.add_argument("disable-inforbars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches",["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  
  driver = webdriver.Chrome(options=options)
  driver.get("https://automated.pythonanywhere.com")
  return driver



def main():
  driver = getDriver()
  element = driver.find_element(by="xpath",value="/html/body/div[1]/div/h1[1]")
  return element.text


print(main())
  