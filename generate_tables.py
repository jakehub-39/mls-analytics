import os
from table_finder import get_table_ids
from scrape_data import scrape_and_save_fbref_data

# Define the URL of the fbref.com page
url = "https://fbref.com/en/squads/64e81410/New-York-City-FC-Stats"

# Call the function to get the list of table IDs
table_ids = get_table_ids(url)

# Specify the base filename, bucket name, and destination path
base_filename = "nycfc"
bucket_name = "fbref_nycfc"
destination_path = "all_stats"

# Iterate over the table IDs
for table_id in table_ids:
    # Generate a unique filename for each table
    filename = f"{base_filename}_{table_id}.csv"

    # Construct the full URL for the specific table
    table_url = f"{url}#{table_id}"

    # Call the function to scrape and save the table data
    scrape_and_save_fbref_data(table_url, filename, bucket_name, destination_path)

    print(f"Table '{table_id}' saved as '{filename}'")

# Remove the temporary CSV files
for table_id in table_ids:
    filename = f"{base_filename}_{table_id}.csv"
    os.remove(filename)

print("Temporary CSV files removed")
