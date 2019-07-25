import inspect
class Navigation:
    def navigate_to_users_page(self, driver, data, homepage, userpage, sShot, lp):
        try:
            data.check_test_status(inspect.stack()[1][3])
            loginData = data.parse_test_data("test_pm_valid_login",1)
            userData = data.parse_test_data(inspect.stack()[1][3],1)
            lp.login_in_to_pm(loginData[0],loginData[1])
            homepage.click_users()
            userpage.click_user_link()
        except:
            sShot.take_screen_shot(inspect.stack()[1][3], driver)
            raise


    def navigate_to_extensions_page(self):
        pass

