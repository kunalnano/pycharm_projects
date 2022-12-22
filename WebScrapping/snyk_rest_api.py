from bs4 import BeautifulSoup
import requests
import csv

# Make an HTTP request to the website
response = requests.get('https://apidocs.snyk.io/?version=2022-12-15#overview')

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the data you want to extract
sections = soup.find_all('div', class_='section')

# Open a CSV file for writing
with open('snyk_api_docs.csv', 'w') as csvfile:
    # Create a CSV writer object
    writer = csv.writer(csvfile)

    # Write the headers to the CSV file
    writer.writerow(['Section Title', 'Section Description'])

    # Loop through the sections
    for section in sections:
        # Extract the data
        title = section.find('h2').text
        description = section.find('p').text

        # Write the data to the CSV file
        writer.writerow([title, description])
