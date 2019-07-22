import pytest
from base.webDriverFactory import  WebDriverFactory

@pytest.yield_fixture()
def setUp():
    print("Runs to set config needed for before every test")
    yield
    print("Runs after every test for clean Up.")

@pytest.yield_fixture(scope="class")
def driver_unit(request, browser):
    print("Setting the class level one time setup configurations")
    if browser == "chrome":
        driver =  WebDriverFactory("chrome").get_driver_instance()
    elif browser == "firefox":
        driver = WebDriverFactory("firefox").get_driver_instance()
    elif browser ==  "ie":
        driver = WebDriverFactory("ie").get_driver_instance()
    else:
        driver =  WebDriverFactory("chrome").get_driver_instance()

    request.cls.driver = driver
    yield
    print("Running the class level one time tearDown configurations")
    driver.quit()

# @pytest.yield_fixture(scope="class")
# def chrome_driver_unit(request):
#     print("Setting the class level one time setup configurations")
#     wdf = WebDriverFactory("chrome")
#     driver = wdf.get_driver_instance()
#     request.cls.driver = driver
#     yield driver
#     print("Running the class level one time tearDown configurations")
#     driver.quit()
#
# @pytest.yield_fixture(scope="class")
# def ie_driver_unit(request):
#     print("Setting the class level one time setup configurations")
#     wdf = WebDriverFactory("ie")
#     driver = wdf.get_driver_instance()
#     request.cls.driver = driver
#     yield driver
#     print("Running the class level one time tearDown configurations")
#     driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


# @pytest.yield_fixture(params=["firefox", "chrome"], scope="class")
# def driver_unit(request):
#     print("Setting the class level one time setup configurations")
#     driver = None
#     if request.param == "chrome":
#         driver = webdriver.Chrome()
#     elif request.param == "firefox":
#         driver = webdriver.Firefox()
#     driver.maximize_window()
#     driver.get("http://10.211.162.111/mp")
#     driver.implicitly_wait(10)
#
#     request.cls.driver = driver
#
#     yield driver
#     print("Running the class level one time tearDown configurations")
#     driver.quit()

