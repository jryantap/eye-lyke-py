
import time
import winsound
from datetime import datetime
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    WebDriverException,
    ElementClickInterceptedException,
)

# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

URL = (
    "https://www.nintendo.com/us/store/products/"
    "nintendo-switch-2-the-legend-of-zelda-"
    "40th-anniversary-edition-121642/"
)

CHECK_INTERVAL = 120  # Seconds between checks

# Dedicated Chrome profile to preserve Nintendo login
PROFILE_PATH = Path(r"C:\NintendoAutoCart\ChromeProfile")

# --------------------------------------------------
# FUNCTIONS
# --------------------------------------------------

def log(message):
    """Print a message with the current time."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}", flush=True)


def notify():
    """Play a Windows notification sound."""
    for _ in range(3):
        winsound.MessageBeep()
        time.sleep(0.5)


def find_add_to_cart(driver):
    """Find an enabled Add to Cart button."""

    xpath = (
        "//button[contains("
        "translate(normalize-space(.), "
        "'ABCDEFGHIJKLMNOPQRSTUVWXYZ', "
        "'abcdefghijklmnopqrstuvwxyz'), "
        "'add to cart')]"
    )

    try:
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        return button

    except TimeoutException:
        return None


# --------------------------------------------------
# CHROME SETUP
# --------------------------------------------------

PROFILE_PATH.mkdir(parents=True, exist_ok=True)

options = webdriver.ChromeOptions()

options.add_argument(
    f"--user-data-dir={PROFILE_PATH}"
)

options.add_argument("--start-maximized")

# Keep the browser visible for manual checkout
driver = webdriver.Chrome(options=options)

# --------------------------------------------------
# MAIN PROGRAM
# --------------------------------------------------

try:
    driver.get(URL)

    log("Nintendo Zelda Auto-Cart Monitor Started!")
    log("Monitoring official Nintendo US store.")

    # First run: sign in manually if necessary
    input(
        "\nMake sure you're signed in to Nintendo. "
        "Press Enter to begin monitoring..."
    )

    while True:

        try:
            log("Checking Add to Cart availability...")

            button = find_add_to_cart(driver)

            if button is not None:

                log("Add to Cart button detected!")

                # Scroll button into view
                driver.execute_script(
                    "arguments[0].scrollIntoView("
                    "{block: 'center'});",
                    button
                )

                time.sleep(1)

                # Automatically click Add to Cart
                button.click()

                log("ADD TO CART CLICKED!")
                log("Check your cart and complete checkout.")

                notify()

                # Stop checking after clicking
                break

            else:
                log("Add to Cart unavailable.")

        except ElementClickInterceptedException:
            log("Button was blocked by another page element.")

        except WebDriverException as error:
            log(f"Browser error: {error}")

        log(f"Next check in {CHECK_INTERVAL} seconds.")
        time.sleep(CHECK_INTERVAL)

        # Refresh Nintendo product page
        try:
            driver.refresh()
        except WebDriverException:
            log("Unable to refresh page. Stopping.")
            break

    # Keep Chrome open for checkout
    input("\nPress Enter to close Chrome...")

finally:
    driver.quit()
