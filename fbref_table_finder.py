import requests
from bs4 import BeautifulSoup

# Define the URL of the fbref.com page
url = "https://fbref.com/en/squads/64e81410/New-York-City-FC-Stats"

# Send a GET request to the URL and get the HTML content
response = requests.get(url)
html = response.content

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(html, 'html.parser')

# Find all table elements on the page and extract their IDs
table_ids = [table.get('id') for table in soup.find_all('table')]

# Print the list of table IDs
for table_id in table_ids:
    print(table_id)