from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


def test_silo_navigation():

    # Chrome options for CI/CD
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # Launch browser
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    # Open website
    driver.get("https://collegedunia.com/university/25451-indira-gandhi-national-open-university-ignou-new-delhi/courses-fees")

    driver.maximize_window()
    time.sleep(3)

    # List of silos
    silos = [
        "Info",
        "Courses & Fees",
        "Admission 2026",
        "Results",
        "IGNOU OPENNET",
        "Reviews",
        "Placement",
        "Ranking",
        "Gallery",
        "Scholarship",
        "Faculty",
        "News & Articles",
        "Hostel",
        "Affiliated Colleges"
    ]

    # Click each silo
    for silo in silos:

        try:
            element = driver.find_element(By.LINK_TEXT, silo)

            driver.execute_script(
                "arguments[0].scrollIntoView();",
                element
            )

            time.sleep(1)

            element.click()

            print(f"{silo} clicked successfully")

            time.sleep(2)

        except Exception as e:
            print(f"Failed to click {silo}")
            print(e)

    # Validation
    assert "ignou" in driver.current_url.lower()

    # Close browser
    driver.quit()