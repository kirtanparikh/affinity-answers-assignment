# Question 2: SQL Query Answers

This document provides the answers to the SQL database questions, based on live execution against the public Rfam database. The full queries can be found in `queries.sql`.

---

### a) Tiger Taxonomy

**i. How many types of tigers can be found in the taxonomy table?**

* **Answer:** **8**
* **Query:**
    ```sql
    SELECT COUNT(*) FROM taxonomy WHERE species LIKE 'Panthera tigris %';
    ```

**ii. What is the "ncbi_id" of the Sumatran Tiger?**

* **Answer:** **9695**
* **Query:**
    ```sql
    SELECT ncbi_id FROM taxonomy WHERE species LIKE 'Panthera tigris sumatrae%';
    ```

---

### b) Connecting Columns in the Database

Based on analyzing the [Rfam database schema](https://docs.rfam.org/en/latest/database.html), the following columns and foreign key relationships are used to connect the tables:

* **`family.rfam_acc`** connects to:
    * `full_region.rfam_acc`
    * `family_literature.rfam_acc`
    * `family_author.rfam_acc`
    * `clan_membership.rfam_acc` (Implied, as it links families to clans)

* **`full_region.rfamseq_acc`** connects to:
    * `rfamseq.rfamseq_acc`

* **`rfamseq.ncbi_id`** connects to:
    * `taxonomy.ncbi_id`

* **`literature_reference.auto_lit`** connects to:
    * `family_literature.auto_lit`

* **`author.auto_author`** connects to:
    * `family_author.auto_author`

* **`clan.clan_acc`** connects to:
    * `clan_membership.clan_acc`

---

### c) Longest Rice DNA Sequence

**Which type of rice has the longest DNA sequence?**

* **Answer:** **Oryza granulata**, with a length of **80,745,213**.
* **Query:**
    ```sql
    SELECT
      t.species,
      r.length
    FROM rfamseq r
    JOIN taxonomy t ON r.ncbi_id = t.ncbi_id
    WHERE
      t.species LIKE 'Oryza %'
    ORDER BY
      r.length DESC
    LIMIT 1;
    ```
* **Result:**
    ```
    +-----------------+----------+
    | species         | length   |
    +-----------------+----------+
    | Oryza granulata | 80745213 |
    +-----------------+----------+
    ```

---

### d) Paginated DNA Sequence Lengths

**Query for the 9th page of families with max DNA sequence length > 1,000,000.**

* **Answer:** The query below joins `family`, `full_region`, and `rfamseq` to find the max length per family, filters, and paginates.
* **Pagination Logic:** `OFFSET 120` (Skip 8 pages * 15 results/page)
* **Query:**
    ```sql
    SELECT f.rfam_acc, f.rfam_id AS family_name, MAX(r.length) AS max_length
    FROM family f
    JOIN full_region fr ON f.rfam_acc = fr.rfam_acc
    JOIN rfamseq r ON fr.rfamseq_acc = r.rfamseq_acc
    GROUP BY f.rfam_acc, f.rfam_id
    HAVING MAX(r.length) > 1000000
    ORDER BY max_length DESC
    LIMIT 15
    OFFSET 120;
    ```
* **Result:**
  ```
  +----------+--------------+------------+
  | rfam_acc | family_name  | max_length |
  +----------+--------------+------------+
  | RF01848  | ACEA_U3      |  836514780 |
  | RF01856  | Protozoa_SRP |  836514780 |
  | RF01911  | MIR2118      |  836514780 |
  | RF03160  | twister-P1   |  836514780 |
  | RF03209  | MIR9657      |  836514780 |
  | RF03674  | MIR5387      |  836514780 |
  | RF03685  | MIR9677      |  836514780 |
  | RF03896  | MIR2275      |  836514780 |
  | RF03926  | MIR1435      |  836514780 |
  | RF04110  | MIR5084      |  836514780 |
  | RF04251  | MIR5070      |  836514780 |
  | RF00145  | snoZ105      |  830829764 |
  | RF00134  | snoZ196      |  801256715 |
  | RF00160  | snoZ159      |  801256715 |
  | RF00202  | snoR66       |  801256715 |
  +----------+--------------+------------+
  15 rows in set (6 min 35.173 sec)
  ```
