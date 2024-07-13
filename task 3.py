import requests
from bs4 import BeautifulSoup

# URL of the static webpage
url = 'http://example.com'

# Send a GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the webpage content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract all text from paragraphs
    print("Paragraphs:")
    paragraphs = soup.find_all('p')
    for p in paragraphs:
        print(p.get_text())
    
    # Extract all links
    print("\nLinks:")
    links = soup.find_all('a', href=True)
    for link in links:
        print(f"URL: {link['href']} Text: {link.get_text()}")
    
    # Extract all images
    print("\nImages:")
    images = soup.find_all('img', src=True)
    for img in images:
        print(f"Image URL: {img['src']}")
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
