import requests
import lxml.html as html
import os
import datetime
import time

def thepiratebay(book):
    try:
        r = requests.get("https://pirateproxy.surf/api",
        params = {"url": f"/q.php?q={book}&cat="})

        links = [f'https://pirateproxy.surf/description.php?id={t["id"]}' 
        for t in r.json()]
        torrents = []
        for link in links:
            re = requests.get(link)
            if re.status_code == 200:
                torrents.append(link)
            else:
                pass
        return torrents

    except ValueError as ve:
        print(f'Error: {ve}')
