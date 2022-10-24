import pytest
import time
from selenium.webdriver.common.by import By
from data.links import Main_Page_URl
from data.page_objects import MainPage, UserPage, ChangeUserPage, UsersCred, LoginPage
from data.credentials import Login

def test_login():
    pytest.driver.get(Main_Page_URl)
    pytest.driver.find_element(By.ID, LoginPage.login_field_id).send_keys(Login.username)
    pytest.driver.find_element(By.ID, LoginPage.password_field_id).send_keys(Login.password)
    pytest.driver.find_element(By.XPATH, LoginPage.submit_button_id).click()

    assert pytest.driver.find_element(By.XPATH, MainPage.page_header_id).text == "Django administration"
    time.sleep(5)

# Add user
def test_create_user():
    pytest.driver.get(Main_Page_URl)
    pytest.driver.find_element(By.XPATH, MainPage.user_list_button).click()
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, UserPage.add_user_button).click()
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, UserPage.user_name_field).send_keys(UsersCred.main_user_name)
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, UserPage.password_field).send_keys(UsersCred.password)
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, UserPage.password_confirmation_field).send_keys(UsersCred.password)
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, UserPage.save_button).click()
    time.sleep(5)

#Update user info
def test_update_user():
    pytest.driver.get(Main_Page_URl)
    pytest.driver.find_element(By.XPATH, MainPage.user_list_button).click()
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, UserPage.search_field).send_keys(UsersCred.main_user_name)
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, UserPage.search_button).click()
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, UserPage.user_data).click()
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, ChangeUserPage.user_name_field).clear()
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, ChangeUserPage.user_name_field).send_keys(UsersCred.changed_user_name)
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, ChangeUserPage.save_button).click()
    time.sleep(5)

# Delete user
def test_delete_user():
    pytest.driver.get(Main_Page_URl)
    pytest.driver.find_element(By.XPATH, MainPage.user_list_button).click()
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, UserPage.search_field).send_keys(UsersCred.changed_user_name)
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, UserPage.search_button).click()
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, UserPage.user_data).click()
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, ChangeUserPage.delete_button).click()
    time.sleep(1)
    pytest.driver.find_element(By.XPATH, ChangeUserPage.submit_delete_button).click()

#Get all users
def get_all_users():
    pytest.driver.get(Main_Page_URl)
    pytest.driver.find_element(By.XPATH, MainPage.user_list_button).click()
    users_list_elem = pytest.driver.find_elements(By.XPATH, UserPage.user_data)
    users_list = []
    for i in users_list_elem:
        users_list.append(i.text)
    return users_list







