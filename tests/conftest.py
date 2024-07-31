import pytest
from pytest_html import extras
from selenium import webdriver
import time
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="edge"
    )
    parser.addoption(
        "--URI", action="store", default="QA"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "edge":
        driver = webdriver.Edge()
    elif browser_name == "IE":
        print("IE driver")

    URI = request.config.getoption("URI")
    if URI == "dev":
        driver.get("https://cloud.appdev.apps.yokogawa.build/app-bdx-host/yibpoc/")
    elif URI == "QA":
        driver.get("https://cloud.appdev.apps.yokogawa.build/app-bdx-host-qa/yibpoc/")
    elif URI == "Stage":
        driver.get("https://cloud.appdev.apps.yokogawa.build/app-bdx-host-stage/yibpoc/workspace")

    driver.implicitly_wait(10)
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extras = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)