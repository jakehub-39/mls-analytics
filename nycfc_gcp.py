import pandas as pd
from google.cloud import storage
from datetime import datetime
import re

# Define the URL of the fbref.com page you want to scrape
url = "https://fbref.com/en/squads/64e81410/New-York-City-FC-Stats"

# Use pandas to read the HTML tables from the page
tables = pd.read_html(url)

# Find the desired table by index or other identification
table = tables[0]  # Adjust the index based on the desired table

# Skip the first row (headers on the second row)
headers = table.iloc[1]
table = table.iloc[2:]

# Define the filename for the CSV file
base_filename = "nycfc_stats.csv"

# Generate a timestamp string
timestamp = datetime.now().strftime("%Y%m%d")

# Append the timestamp to the base filename
filename = re.sub(r"\.csv$", f"_{timestamp}.csv", base_filename)

# Save the table data as a CSV file with headers
table.to_csv(filename, index=False, header=True)

# Set up Google Cloud Storage client
client = storage.Client()

# Define the name of the bucket and the destination blob path
bucket_name = "fbref_nycfc"
blob_name = "all_stats/" + filename

# Upload the CSV file to the Google Cloud Storage bucket
bucket = client.bucket(bucket_name)
blob = bucket.blob(blob_name)
blob.upload_from_filename(filename)

print ("File " + filename + " uploaded to Google Cloud Storage successfully!")
