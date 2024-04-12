import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the Flipkart mobile section
url = 'https://www.shopsy.in/search?q=speaker&marketplace=FLIPKART&as-show=on&pageUID=1712931589445'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the mobile speakers listed on the page
speakers = soup.find_all('div', class_='css-1dbjc4n r-13awgt0')

# Create lists to store the details of each speaker
names = []
prices = []

# Extract details of each speaker and store them in the lists
for speaker in speakers:
    name = speaker.find('span', class_='css-901oao css-16my406 r-op4f77 r-1et8rh5 r-1enofrn r-14yzgew r-zl2h9q r-1udh08x').text
    price = speaker.find('div', class_='css-901oao r-cqee49 r-1vgyyaa r-1b43r93 r-1rsjblm r-13hce6t')
    # rating = speaker.find('div', class_='_3LWZlK').text if speaker.find('div', class_='_3LWZlK') else None
    names.append(name)
    prices.append(price)
    # ratings.append(rating)

# Create a DataFrame using the lists
data = {'Name': names, 'Price': prices}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
df.to_csv('shopsy.csv')
