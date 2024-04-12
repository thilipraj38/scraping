import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Flipkart mobile section
url = 'https://www.flipkart.com/search?q=speaker&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the mobile speakers listed on the page
speakers = soup.find_all('div', class_='_4ddWXP')

# Create lists to store the details of each speaker
names = []
prices = []

# Extract details of each speaker and store them in the lists
for speaker in speakers:
    name = speaker.find('a', class_='s1Q9rs').text
    price = speaker.find('div', class_='_30jeq3').text
    # rating = speaker.find('div', class_='_3LWZlK').text if speaker.find('div', class_='_3LWZlK') else None
    names.append(name)
    prices.append(price)
    # ratings.append(rating)

# Create a DataFrame using the lists
data = {'Name': names, 'Price': prices}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
df.to_csv('flipkart.csv')
