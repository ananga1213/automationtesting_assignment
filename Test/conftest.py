import pytest
from selenium import webdriver
from Utilities import loaddata
from Utilities.Masterclass import Masterclass

driver = None

path = ("..//Files//testdata.xlsx")

log=Masterclass.getLogger(self=driver)


@pytest.fixture(scope="class")
def browser(request):
    global driver
    rows = loaddata.getRowCount(path, "selectBrowser")
    for r in range(2, rows+1):
        if loaddata.readData(path,"selectBrowser", r, 2) == "T":
            try:
                browserName = loaddata.readData(path,"selectBrowser", r, 1)
                log.info("Browser selected is/are : " +browserName)
            except Exception as e:
                raise
            if browserName == "chrome":
                try:
                    driver = webdriver.Chrome(executable_path="../Files/chromedriver.exe")
                    log.info("Running script on "+browserName+ "browser")
                except Exception as e:
                    raise
            elif browserName == "Firefox":
                try:
                    driver = webdriver.Firefox(executable_path="../Files/geckodriver.exe")
                    log.info("Running script on " + browserName + "browser")
                except Exception as e:
                    raise
            elif browserName == "Ie":
                try:
                    driver = webdriver.Ie(executable_path="../Files/IEDriverServer.exe")
                    log.info("Running script on " + browserName + "browser")
                except Exception as e:
                    raise
            url = loaddata.readData(path, "url", 2, 1)
            driver.get(url)
            log.info("URl entered is " + url)
            driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.mark.hookwrapper
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
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)
