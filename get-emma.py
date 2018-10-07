# model scraping for themodelbot

import requests #allows to make requests to webpages
from bs4 import BeautifulSoup as bs #downloading the html that makes up the webpages so we can easily parse through that
import os #to create folder that we are in

# website with model images
url = 'https://www.gettyimages.in/photos/emma-watson?mediatype=photography&phrase=emma%20watson&sort=mostpopular'

# download page for parsing
page = requests.get(url) #requesting a response from the server
soup = bs(page.text, 'html.parser') #html that makes up that website that we requested

# locate all elements with image tag
image_tags = soup.findAll('img') #bs4 method to findall image tags and returns its list

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
        url = image['src'] #extracting the source url of that image
        source = requests.get(url)
        if source.status_code == 200: #if we get a response
            with open('Emma-' + str(x) + '.jpg', 'wb') as f: #create the jpg file and write to it
                f.write(requests.get(url).content) #write to the image that we get when we go to that url
                f.close()
                x += 1
    except:
        pass