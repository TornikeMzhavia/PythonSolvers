import urllib.request
import requests
import os
from bs4 import BeautifulSoup

buzz_url = 'https://www.buzzfeed.com/davidmack/photos-from-a-chinese-steel-mill'
user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
download_dir = r'C:\Users\Tornike\Downloads\buzz'

page = requests.get(buzz_url, headers={'user-agent': user_agent}).content
print('Page downloaded. retrieving urls...')

bs = BeautifulSoup(page, 'lxml')
image_urls = (link.attrs['rel:bf_image_src'] for link in bs.find_all('img') if 'rel:bf_image_src' in link.attrs)
print('Got image urls. Downloading...')

for ind, image_url in enumerate(image_urls):
    status = urllib.request.urlretrieve(image_url, os.path.join(download_dir, str(ind) + '.jpg'))
    print('Status: {} at index: {}'.format(status, ind))