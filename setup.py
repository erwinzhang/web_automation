from selenium import webdriver
from selenium.webdriver.common.keys import Keys

server = "https://mobile-pf-test.blackboard.com"
driver = webdriver.Firefox()
coursename = 'discussionTesting: DiscussionTestingCourse'

username='stud01'
password='123'

def open_browser(server):
    driver.get(server)

def close_browser():
    driver.close()


def login(username,password):
    username_txf = driver.find_element_by_id('user_id')
    password_txf = driver.find_element_by_name('password')
    login_btn = driver.find_element_by_id('entry-login')
    username_txf.send_keys(username)
    password_txf.send_keys(password)
    login_btn.click()

def courses_menu():
    return driver.find_element_by_id('Courses.label')

def click_course(coursename):
    driver.find_element_by_link_text(coursename).click()

def discussions_menu():
    return driver.find_element_by_xpath(".//span[contains(text(), 'Discussions')]")

open_browser(server)
# login(username,password)
# courses_menu().click()
# click_course(coursename)
# discussions_menu().click()
print driver.session_id
print driver.current_url

#close_browser()
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()