import requests
import os
import play_scraper
import time

from PIL import Image
from google_play_scraper import app

pages = input("Pages do you want to scrape : ")
count_input = input("App count do you want to scrape : ")
search_term = input("Search term : ")
folder_location = input("folder location : ")

search_results = play_scraper.search(search_term, page=pages)
count = int(count_input)

for item in search_results:

    count = count + 1
    if count == 15:
        break

    result = app(
        item["app_id"],
        lang='en',
        country='us'
    )

    path = os.path.join(folder_location, result["title"])
    os.makedirs(path, exist_ok=True)

    i = 1
    screenshots = result["screenshots"]

    for x in screenshots:
        final_url = x + "=w3840-h1886"
        print(final_url)
        r = requests.get(final_url, allow_redirects=True)
        name = path + "/" + "screenshot" + str(i)
        open(name + ".webp", 'wb').write(r.content)
        im = Image.open(name + ".webp").convert("RGB")
        im.save(name + ".png", "png")
        os.remove(name + ".webp")
        i = i + 1

    time.sleep(3)
