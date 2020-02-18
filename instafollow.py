import itertools
from time import *
from explicit import waiter, XPATH
from selenium import webdriver
from selenium.webdriver.common.by import By
import json

def login(driver):
	driver.get('https://www.instagram.com/accounts/login')
	sleep(20)

def scrape_followers(driver, account):
	# Load account page
	driver.get("https://www.instagram.com/{0}/".format(account))

	# Click the 'Follower(s)' link
	# driver.find_element_by_partial_link_text("follower").click()
	driver.find_element_by_xpath("//a[@href='/{0}/followers/']".format(account)).click()
	#driver.find_element(By.PARTIAL_LINK_TEXT, 'followers').click()
	input()
	# Wait for the followers modal to load
	driver.find_element_by_xpath("//div[@role='dialog']")

	follower_css = "ul div li:nth-child({}) a.notranslate"  # Taking advange of CSS's nth-child functionality
	for group in itertools.count(start=1, step=30):
		for follower_index in range(group, group + 30):
			print(waiter.find_element(driver, follower_css.format(follower_index)).text)
		last_follower = driver.find_element(driver, follower_css.format(follower_index))
		driver.execute_script("arguments[0].scrollIntoView();", last_follower)
if __name__ == "__main__":
	account = 'gowtham_18_'
	driver = webdriver.Firefox()
	try:
		login(driver)
		# Print the first 75 followers for the "instagram" account
		print('Followers of the "{}" account'.format(account))
		print(enumerate(scrape_followers(driver, account=account), 1))
		for count,follower in enumerate(scrape_followers(driver, account=account), 1):
			print("\t{}: {}".format(count,follower))
			if count >= 75:
				break
	finally:
		driver.quit()
