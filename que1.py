import requests
from bs4 import BeautifulSoup

url = "https://allevents.in"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

events = []

for event in soup.find_all('div', class_='event-card'):
    title = event.find('h3', class_='event-title').get_text(strip=True)
    date_time = event.find('div', class_='event-date-time').get_text(strip=True)
    location = event.find('div', class_='event-location').get_text(strip=True)
    description = event.find('div', class_='event-description').get_text(strip=True)
    price = event.find('div', class_='event-price').get_text(strip=True)
    
    events.append({
        'Title': title,
        'Date, Time': date_time,
        'Location': location,
        'Description': description,
        'Price': price
    })

for event in events:
    print(event)