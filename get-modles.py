# model scraping for themodelbot

import requests
from bs4 import BeautifulSoup as bs
import os

# website with model images
url = 'https://www.gettyimages.in/photos/emma-watson?mediatype=photography&phrase=emma%20watson&sort=mostpopular'

# download page for parsing
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# locate all elements with image tag
image_tags = soup.findAll('img')

# create directory for model images
if not os.path.exists('EmmaWatson'):
    os.makedirs('EmmaWatson')

# move to new directory
os.chdir('EmmaWatson')

# image file name variable
x = 0

# writing images
for image in image_tags:
    try:
        url = image['src']
        response = requests.get(url)
        if response.status_code == 200:
            with open('Emma-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass