import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from tabulate import tabulate
import sys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    print("Setting up headless Chrome driver...")
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("log-level=3")

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    chrome_options.add_argument(f"user-agent={user_agent}")

    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.set_page_load_timeout(30)
        return driver
    except Exception as e:
        print(f"Error setting up WebDriver: {e}")
        sys.exit(1)

def scrape_olx_data(driver, url):
    try:
        print(f"Opening {url}...")
        driver.get(url)

        # This will wait UP TO 15 seconds for the ads to appear.
        # We are using the class _1DNjI from your HTML.
        print("Waiting for ad content to load...")
        wait = WebDriverWait(driver, 15)
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "li._1DNjI")))

    except Exception as e:
        print(f"Error loading page or finding content: {e}")
        print("\n--- DEBUG: Page HTML ---")
        print(driver.page_source)
        print("\n--- END DEBUG ---")
        return []

    print("Scraping ad data...")
    results = []

    ad_cards = driver.find_elements(By.CSS_SELECTOR, "li._1DNjI")

    if not ad_cards:
        print("No ad cards found, even after waiting.")
        return []

    for card in ad_cards:
        try:
            title_element = card.find_element(By.CSS_SELECTOR, "span[data-aut-id='itemTitle']")
            price_element = card.find_element(By.CSS_SELECTOR, "span[data-aut-id='itemPrice']")

            title = title_element.text
            price = price_element.text

            if title and price:
                results.append([title, price])
        except Exception:
            # This will skip "Featured" ads or other junk that doesn't have a price
            pass

    return results

def main():
    SEARCH_URL = "https://www.olx.in/items/q-car-cover?isSearchCall=true"
    driver = setup_driver()

    if driver:
        data = scrape_olx_data(driver, SEARCH_URL)
        driver.quit()
        print("Driver closed.")

        if data:
            print(f"\n--- Found {len(data)} Results ---")
            headers = ["Title", "Price"]
            print(tabulate(data, headers=headers, tablefmt="grid"))
        else:
            print("No data was successfully scraped.")

if __name__ == "__main__":
    main()
