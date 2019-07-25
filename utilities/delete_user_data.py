from pages.pom_pm_user_page import PM_Users_Page
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import inspect
from selenium.webdriver.common.by import By
class Delete_User_Data:
    def delete_data(self, pmhomepage, userpage, driver, userName, sShot):
        try:
            pmhomepage.click_users()
            userpage.click_user_link()
            userpage.get_element(userpage.__user_name_input_range__,"name").clear()
            userpage.set_user_name_input_range(userName)
            userpage.click_user_view_button()
            element = driver.find_element(By.XPATH, "(//td[contains(text(),'"+userName+"')])[1]//preceding-sibling::td[18]")
            element.click()
            driver.switch_to_alert().accept()
            actMessage = userpage.get_text(userpage.__user_delete_actual_msg__, "class").strip()
            result = userpage.text_equals(actMessage, userpage.__user_delete_expected_msg__)
            assert result, "Deletion is not successful"
        except:
            sShot.take_screen_shot(inspect.stack()[1][3], driver)
            raise