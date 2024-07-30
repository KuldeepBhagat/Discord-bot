import requests
from bs4 import BeautifulSoup
import re

class PirateBay:

    def __init__(self, query, page_number=1):
        link = query.replace(' ', '%20')
        self.search_url = f"https://mirrorbay.org/search/keywords:{link}/?page={page_number}"
    
    def extract_magnet(self):
        magnet = []
        response = requests.get(self.search_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        magnet_link = soup.find_all('a', href=True)
        for html in magnet_link:
            if html['href'].startswith('magnet:'):
                magnet.append(html['href'])
        return magnet
    
    def extract_title(self):
        title = []
        response = requests.get(self.search_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all('span', class_="list-item item-name item-title")
        for html in data:
            anchor = html.find('a')
            title.append(anchor.text)
        return title
    
    def extract_info(self, sites):
        response = requests.get(sites)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find('label', id='s')
        seed = data.text
        data = soup.find('label', id='l')
        leech = data.text
        data = soup.find('label', id='nfiles')
        no_files = data.text
        data = soup.find('label', id='size')
        size = data.text
        data = soup.find('label', id='cat')
        type = data.text
        data = soup.find('label', id='uld')
        date = data.text
        data = soup.find('label', id='user')
        user = data.text
        return seed, leech, no_files, size, type, date, user
    
    def extract_page(self):
        response = requests.get(self.search_url)
        sites = []
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all('span', class_="list-item item-name item-title",)
        for html in data:
            anchor = html.find('a')
            link = anchor.get('href')
            sites.append('https://mirrorbay.org/'+link)
        return sites

class nyaa:
    def __init__(self, query, page_number=1):
        link = query.replace(' ', '+')
        self.search_url = f"https://nyaa.si/?f=0&c=0_0&q={link}&p={page_number}"
    
    def extract_mag_and_tor(self):
        magnet = []
        torrent = []
        response = requests.get(self.search_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all('a', href=True)
        for html in data:
            if html['href'].startswith('magnet:'):
                magnet.append(html['href'])
            if html['href'].startswith('/download'):
                torrent.append("https://nyaa.si/"+html['href'])
        return magnet, torrent
    
    def extract_title_and_type(self):
        title = []
        type = []
        response = requests.get(self.search_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all('a')
        for name in data:
            if name.get('title') == None:
                continue
            elif name.get('title').startswith('Anime') or name.get('title').startswith('Literature'):
                type.append(name.get('title'))
                continue
            elif 'comment' in name.get('title').lower():
                continue
            title.append(name.get('title'))
        return title, type
    
    def extract_info(self):
        size = []
        date= []
        seed = []
        leech = []
        no_of_down = []
        response = requests.get(self.search_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all('td', class_='text-center', href=False)
        temp = []
        for info in data:
            if info.find('a'):
                continue
            temp.append(info.text)
            if len(temp) == 5:
                size.append(temp[0])
                date.append(temp[1])
                seed.append(temp[2])
                leech.append(temp[3])
                no_of_down.append(temp[4])
                temp.clear()
        return size, date, seed, leech, no_of_down
    
    def extract_page(self):
        site = []
        response = requests.get(self.search_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all('a', href=True)
        for link in data:
            if link['href'].startswith('/view'):
                if link['href'].endswith('#comments'):
                    continue
                site.append('https://nyaa.si/' + link['href'])
        return site