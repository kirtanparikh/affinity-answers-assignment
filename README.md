# Affinity Answers - Engineering Assignment

Hello! This repository contains my solutions for the technical assignment. I've organized each question into its own folder.

Thank you for the opportunity.

---

## 1. Q1: Python Web Scraper (OLX)

This script scrapes ad data from an OLX search results page.

* **Folder:** `q1_python_scraper/`
* **Technology:** Uses **Selenium** to control a headless Chrome browser, as OLX is a JavaScript-heavy site. This allows the script to wait for content to load, just as a user would.
* **Note:** The script scrapes **Title** and **Price**. The "Description" is not available on the search results page and would require a much more complex scraper to visit each ad link.

### How to Run:
```bash
cd q1_python_scraper
pip install -r requirements.txt
python main.py
```

---

## 2. Q2: SQL Queries (Rfam Database)

This folder contains the SQL queries and their answers from the live public Rfam database.

* **Folder:** `q2_sql_queries/`
* **Queries:** `queries.sql` contains the complete, commented SQL for all parts.
* **Answers:** `answers.md` contains the formatted answers, the schema analysis, and the *actual results* from running the queries.

---

## 3. Q3: Shell Script (AMFI NAV Data)

This script extracts "Scheme Name" and "Asset Value" from an AMFI data file and saves them as a `.tsv`.

* **Folder:** `q3_shell_script/`
* **Technology:** Uses `curl` to fetch and `awk` to parse the data for efficiency.

### How to Run:
```bash
cd q3_shell_script
chmod +x get_nav.sh
./get_nav.sh
```
This will create a `nav_data.tsv` file. The folder's `README.md` also contains my analysis on why TSV/CSV is a better format than JSON for this data.
