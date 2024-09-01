import requests
from bs4 import BeautifulSoup

# Start a session
session = requests.Session()

# Login URL
login_url = 'https://example.com/login'

# Data to be sent for login (check the form data required by the website)
payload = {
    'username': 'your_username',
    'password': 'your_password'
}

# Post request to log in
session.post(login_url, data=payload)

# URL to the result page
result_url = 'https://example.com/dashboard/results'

# Get the result page
response = session.get(result_url)

# Parse the result using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the desired result
result = soup.find('div', {'id': 'result-id'}).text  # Adjust according to the site's structure

print(result)
