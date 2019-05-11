from selenium import webdriver
from selenium.webdriver.common.keys import Keys   # for necessary browser action
from selenium.webdriver.common.by import By    # For selecting html code
from Trendyol import Trendyol

options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options , executable_path="/home/askari/Documents/komtas/Selenium/chromedriver")

driver.get("https://www.trendyol.com/erkek+t-shirt")

data = driver.find_elements_by_css_selector('div[class="p-card-wrppr"]')

clothes = []

for a in data:

	buy_url = a.find_element_by_css_selector('a').get_attribute("href")
	img_url = a.find_element_by_css_selector('img').get_attribute("src")
	company_name = a.find_element_by_css_selector('span').get_attribute("innerHTML")
	# old_price = a.find_element_by_css_selector('div[class="prc-box-sllng"]')#.get_attribute("innerHTML")

	print(company_name)
	# print(old_price)

	trendyol = Trendyol(buy_url , img_url , company_name , 10)

	clothes.append(trendyol)


print (clothes)

driver.close()