-- =============================================================================
-- Affinity Answers Assignment - Question 2
-- =============================================================================

--
-- Question 2a(i): How many types of tigers can be found in the taxonomy table?
--
SELECT COUNT(*) AS tiger_subspecies_count
FROM taxonomy
WHERE species LIKE 'Panthera tigris %';

--
-- Question 2a(ii): What is the "ncbi_id" of the Sumatran Tiger?
-- We use LIKE to account for potential padding or extra descriptions.
--
SELECT ncbi_id
FROM taxonomy
WHERE species LIKE 'Panthera tigris sumatrae%';

--
-- Question 2c: Which type of rice has the longest DNA sequence?
--
SELECT t.species, r.length
FROM rfamseq r
JOIN taxonomy t ON r.ncbi_id = t.ncbi_id
WHERE t.species LIKE 'Oryza %'
ORDER BY r.length DESC
LIMIT 1;

--
-- Question 2d: Paginated Family DNA Sequence Lengths
--
-- This query joins family -> full_region -> rfamseq to link
-- families to their sequence lengths.
--
-- Pagination Logic: 9th page, 15 results/page
-- Offset = (9 - 1) * 15 = 120
--
SELECT f.rfam_acc, f.rfam_id AS family_name, MAX(r.length) AS max_length
FROM family f
JOIN full_region fr ON f.rfam_acc = fr.rfam_acc
JOIN rfamseq r ON fr.rfamseq_acc = r.rfamseq_acc
GROUP BY f.rfam_acc, f.rfam_id
HAVING MAX(r.length) > 1000000
ORDER BY max_length DESC
LIMIT 15
OFFSET 120;
