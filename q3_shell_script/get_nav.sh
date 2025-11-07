#!/bin/bash

# --- Configuration ---
URL="https://www.amfiindia.com/spages/NAVAll.txt"
OUTPUT_FILE="nav_data.tsv"

# --- Main Logic ---
echo "Fetching data from $URL..."

# Use curl to fetch, awk to process
# -F';' sets the delimiter to a semicolon
# OFS='\t' sets the output field separator to a tab
# We filter out lines that don't look like data (e.g., empty, headers)
curl -sL "$URL" | awk -F';' 'BEGIN {OFS="\t"} {
    # Skip empty lines and header lines
    if (NF == 6 && $1 ~ /^[0-9]+$/ && $5 != "" && $5 ~ /^[0-9.]+$/) {
        print $4, $5
    }
}' > "$OUTPUT_FILE"

# Check if curl succeeded and file was created
if [ $? -eq 0 ] && [ -s "$OUTPUT_FILE" ]; then
    echo "Data saved to $OUTPUT_FILE"
    echo "Total records: $(wc -l < "$OUTPUT_FILE")"
else
    echo "Error: Failed to fetch or process data"
    exit 1
fi
