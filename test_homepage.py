from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import requests
import time


def test_collegedunia_ui_validation():

    print("\n========== TEST STARTED ==========\n")

    # ---------------------------------------------------
    # Chrome Setup
    # ---------------------------------------------------

    options = Options()

    # Keep browser visible
    # options.add_argument("--headless")

    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.implicitly_wait(10)

    wait = WebDriverWait(driver, 10)

    # ---------------------------------------------------
    # URL
    # ---------------------------------------------------

    url = "https://collegedunia.com/university/25451-indira-gandhi-national-open-university-ignou-new-delhi/master-of-arts-ma-part-time"

    driver.get(url)

    driver.maximize_window()

    print("URL Opened Successfully")
    print("Current URL:", driver.current_url)

    # ---------------------------------------------------
    # 1. Banner Validation
    # ---------------------------------------------------

    print("\n========== BANNER VALIDATION ==========")

    try:

        banners = driver.find_elements(By.TAG_NAME, "img")

        if len(banners) > 0:
            print(f"[PASS] Total Images Found: {len(banners)}")
        else:
            print("[FAIL] No Images Found")

    except Exception as e:
        print("[FAIL] Banner Validation Failed")
        print(e)

    # ---------------------------------------------------
    # 2. Broken Images Validation
    # ---------------------------------------------------

    print("\n========== IMAGE VALIDATION ==========")

    images = driver.find_elements(By.TAG_NAME, "img")

    broken_images = 0

    for img in images:

        src = img.get_attribute("src")

        if src:

            try:

                response = requests.get(src, timeout=5)

                if response.status_code != 200:
                    broken_images += 1
                    print(f"[BROKEN IMAGE] {src}")

            except:
                broken_images += 1
                print(f"[BROKEN IMAGE] {src}")

    if broken_images == 0:
        print("[PASS] No Broken Images Found")
    else:
        print(f"[FAIL] Total Broken Images: {broken_images}")

    # ---------------------------------------------------
    # 3. CTA Button Validation
    # ---------------------------------------------------

    print("\n========== CTA BUTTON VALIDATION ==========")

    buttons = driver.find_elements(By.TAG_NAME, "button")

    if len(buttons) > 0:
        print(f"[PASS] Total CTA Buttons Found: {len(buttons)}")
    else:
        print("[FAIL] No CTA Buttons Found")

    # ---------------------------------------------------
    # 4. Navigation Validation
    # ---------------------------------------------------

    print("\n========== NAVIGATION VALIDATION ==========")

    silos = [
        "Info",
        "Courses & Fees",
        "Admission 2026",
        "Reviews",
        "Placement",
        "Ranking"
    ]

    for silo in silos:

        try:

            element = wait.until(
                EC.presence_of_element_located(
                    (By.PARTIAL_LINK_TEXT, silo)
                )
            )

            driver.execute_script(
                "arguments[0].scrollIntoView({block:'center'});",
                element
            )

            time.sleep(1)

            element.click()

            time.sleep(2)

            print(f"[PASS] {silo} Navigation Working")

        except Exception as e:

            print(f"[FAIL] {silo} Navigation Failed")
            print(e)

    # ---------------------------------------------------
    # 5. Search Bar Validation
    # ---------------------------------------------------

    print("\n========== SEARCH BAR VALIDATION ==========")

    search_boxes = driver.find_elements(By.TAG_NAME, "input")

    if len(search_boxes) > 0:
        print(f"[PASS] Input/Search Fields Found: {len(search_boxes)}")
    else:
        print("[FAIL] Search Bar Not Found")

    # ---------------------------------------------------
    # 6. Slider Validation
    # ---------------------------------------------------

    print("\n========== SLIDER VALIDATION ==========")

    sliders = driver.find_elements(By.CLASS_NAME, "swiper")

    if len(sliders) > 0:
        print(f"[PASS] Sliders Found: {len(sliders)}")
    else:
        print("[INFO] No Sliders Detected")

    # ---------------------------------------------------
    # 7. Mobile Responsiveness
    # ---------------------------------------------------

    print("\n========== MOBILE RESPONSIVENESS ==========")

    driver.set_window_size(375, 812)

    time.sleep(2)

    mobile_width = driver.execute_script(
        "return window.innerWidth;"
    )

    print(f"[PASS] Mobile Width Applied: {mobile_width}")

    # ---------------------------------------------------
    # 8. Footer Links Validation
    # ---------------------------------------------------

    print("\n========== FOOTER LINKS VALIDATION ==========")

    links = driver.find_elements(By.TAG_NAME, "a")

    print(f"Total Links Found: {len(links)}")

    broken_links = 0

    for link in links[:20]:

        href = link.get_attribute("href")

        if href and href.startswith("http"):

            try:

                response = requests.get(href, timeout=5)

                if response.status_code >= 400:
                    broken_links += 1
                    print(f"[BROKEN LINK] {href}")

            except:
                broken_links += 1
                print(f"[BROKEN LINK] {href}")

    if broken_links == 0:
        print("[PASS] Footer Links Working")
    else:
        print(f"[FAIL] Broken Links Found: {broken_links}")

    # ---------------------------------------------------
    # Final Result
    # ---------------------------------------------------

    print("\n========== FINAL TEST RESULT ==========")

    print("""
TESTED FEATURES:
1. Banner loading
2. Broken images/icons
3. CTA buttons
4. Navigation menu
5. Search bar
6. Sliders/carousels
7. Mobile responsiveness
8. Footer links
""")

    print("Automation Testing Completed Successfully")

    # Keep browser open for 10 seconds
    time.sleep(10)

    driver.quit()


# ---------------------------------------------------
# MAIN FUNCTION CALL
# ---------------------------------------------------

