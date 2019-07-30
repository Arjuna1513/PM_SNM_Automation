# from pages.pom_pm_user_page import PM_Users_Page
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
import inspect
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec
from selenium.webdriver.common.by import By


class Delete_User_Data:
    def delete_data(self, pmhomepage, userpage, driver, userName, sShot):
        try:
            wait = WebDriverWait(driver, 30)
            pmhomepage.click_users()
            userpage.click_user_link()
            userpage.get_element(userpage.__user_name_input_range__,"name").clear()
            userpage.set_user_name_input_range(userName)
            userpage.click_user_view_button()
            wait.until(ec.presence_of_element_located((By.ID,"removeThis0_img")))
            element = driver.find_element(By.ID,"removeThis0_img")
            element.click()
            driver.switch_to_alert().accept()
            actMessage = userpage.get_text(userpage.__user_delete_actual_msg__, "class").strip()
            result = userpage.text_equals(actMessage, userpage.__user_delete_expected_msg__)
            assert result, "Deletion is not successful"
        except:
            sShot.take_screen_shot(inspect.stack()[1][3], driver)
            raise