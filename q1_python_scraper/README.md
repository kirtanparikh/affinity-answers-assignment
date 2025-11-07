# Question 1: Python Web Scraper

This directory contains the Python script to scrape "Car Cover" ads from OLX.

### How to Run

1.  **Install Dependencies:**
    Make sure you have Python 3 and Google Chrome installed.
    ```bash
    # Navigate to this directory
    cd q1_python_scraper

    # Install required libraries
    pip install -r requirements.txt
    ```

2.  **Run the Script:**
    ```bash
    python main.py
    ```
    The script will start a headless (invisible) Chrome browser, scrape the data, and print the **Title** and **Price** in a table format.

### Technical Choices

* **Selenium vs. Requests/BeautifulSoup:**
    OLX is a modern JavaScript-driven website. A simple scraper using `requests` would only receive the initial HTML *before* the ad listings are loaded. **Selenium** is used here because it can control a real browser, execute the JavaScript, and wait for the content to appear, allowing us to scrape the data as a user would see it. This is the correct tool for this specific job.

* **`webdriver-manager`:**
    This library is used to automatically download and manage the `chromedriver` executable, eliminating any manual setup for the person running the code.

### Note on "Description"

The assignment asked for **Title, Description, and Price**.
* **Title** and **Price** are available on the search results page and are successfully scraped.
* **Description** is **not** available on the search results page. To get the description, the scraper would have to click on *each individual ad*, load a new page, and find the description, then go back.

This is a much more complex and time-consuming operation. For this assignment, I have focused on efficiently scraping all the data available on the main search page.
