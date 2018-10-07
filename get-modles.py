# scraping codes

import requests
from bs4 import BeautifulSoup as bs
import os

#websites with modles

url = "https://www.gettyimages.in/photos/emma-watson?sort=mostpopular&mediatype=photography&phrase=emma%20watson"

#downloading page from parsing

page = requests.get(url)
soup = bs(page.txt , 'html.parser')

#locate all image with image tag 

image_tags = soup.findall('img')

#create directory for pics

if not os.path.exists('EmmaWatson'):
	os.makedirs('EmmaWatson')

#move to new directory

os.chdir('EmmaWatson')

#image file name variable

x=0

#writing image

for image in image_tags:
	try:
		url = image['src']
		source = requests.get(url)
		if source.status_code == 200: #if we get a response
			with open('EmmaWatson-' + str(x) + '.jpg' + 'wb') as f:
				f.write(requests.get(url).content)
				f.close()
				x = x+1
	except:
		pass