from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_xpath():

    # Chrome setup
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Launch browser
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    # Explicit wait
    wait = WebDriverWait(driver, 10)

    # Open website
    driver.get("https://www.saucedemo.com/")

    print("Website opened successfully")

    # Locate username field using XPath
    username = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='user-name']")
        )
    )

    print("Username field located successfully")

    # Locate password field
    password = driver.find_element(
        By.XPATH,
        "//input[@id='password']"
    )

    print("Password field located successfully")

    # Locate login button
    login = driver.find_element(
        By.XPATH,
        "//input[@id='login-button']"
    )

    print("Login button located successfully")

    # Enter credentials
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")

    print("Credentials entered successfully")

    # Click login
    login.click()

    print("Login button clicked successfully")

    # Validate successful login
    wait.until(
        EC.url_contains("inventory")
    )

    assert "inventory" in driver.current_url

    print("Login successful using XPath")
    print("Current URL:", driver.current_url)

    # Close browser
    driver.quit()