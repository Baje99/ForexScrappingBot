from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument('--start-maximized')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--log-level=1')
options.add_argument("–disable-extensions")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36")
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = options)
driver.get("https://www.forexfactory.com/")
time.sleep(4)
items = driver.find_elements(By.TAG_NAME, "tr")
for x in items:
    try:
        x.find_element(By.CLASS_NAME, 'high')
        tdclass = x.find_elements(By.TAG_NAME, "td")
        if "USD" in tdclass[3].text:
            dict = {"Time" : "Not Found",
                    "Currency" : "USD",
                    "Title" : "Not found",
                    "Actual" : "Not found",
                    "Forecast" : "Not found",
                    "Previous" : "Notfound"}
            if tdclass[1].text:
                dict["Time"] = tdclass[1].text
            if tdclass[5].text:
                dict["Title"] = tdclass[5].text
            if tdclass[7].text:
                dict["Actual"] = tdclass[7].text
            if tdclass[8].text:
                dict["Forecast"] = tdclass[8].text
            if tdclass[9].text:
                dict["Previous"] = tdclass[9].text
            print(dict)

    except Exception as e:
        continue
driver.close()