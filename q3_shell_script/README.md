# Question 3: Shell Script

This directory contains the solution for the shell scripting task.

### How to Run

1.  Make sure you are in the `q3_shell_script` directory.
2.  Make the script executable (if you haven't already):
    ```bash
    chmod +x get_nav.sh
    ```
3.  Run the script:
    ```bash
    ./get_nav.sh
    ```

This will fetch the latest data and create a file named `nav_data.tsv` in this directory.

---

### Follow-up: Should this data be stored in JSON?

This is a classic question of using the right tool for the job. While JSON is an excellent format, a delimited format (like TSV or CSV) is far more appropriate for this specific use case.

Here’s a brief analysis:

**1. Data Structure:**
The data is a simple, flat, two-dimensional table. It has no nested elements, hierarchies, or complex relationships. It is the very definition of tabular data.

**2. Efficiency and Overhead:**
* **TSV (Current):** This format is extremely lightweight. The only overhead is a single tab character (`\t`) per row.
* **JSON:** To store this data, you would likely use an array of objects:
    ```json
    [
      {"Scheme Name": "...", "Asset Value": "..."},
      {"Scheme Name": "...", "Asset Value": "..."},
      ...
    ]
    ```
    For **every single row**, JSON adds significant overhead ( `{"`, `": "`, `", "`, `": "`, `"},` ). For a file with tens of thousands of rows, this overhead would dramatically increase the file size, making it slower to download and parse.

**3. Tooling and Use Case:**
* **TSV/CSV:** The primary use for this file is likely bulk analysis. Delimited files can be directly streamed and processed by nearly every data tool on the planet (like `awk`, Python's `pandas`, Excel, or any database loader) with maximum efficiency.
* **JSON:** Parsing JSON requires a dedicated JSON parser, which loads the data into memory. While fast, it's an unnecessary step for the simple task of "get the 4th and 5th columns."

**Conclusion:**

No, this data should not be stored in JSON.

The current semicolon-delimited format (which our script converts to TSV) is the optimal choice. It prioritizes **low overhead**, **fast processing**, and **universal compatibility** for a large, simple, tabular dataset.

JSON is the right choice for API responses, configuration files, or data with a nested/hierarchical structure, none of which apply here.
