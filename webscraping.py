import requests
from bs4 import BeautifulSoup
# Import MongoClient from pymongo so we can connect to the database
from pymongo import MongoClient




if __name__ == '__main__':
    # Instantiate a client to our MongoDB instance
    db_client = MongoClient('mongodb://localhost:27017')
    bdd3 = db_client.bdd3
    rt = bdd3.rt


    response = requests.get("https://actualidad.rt.com")
    soup = BeautifulSoup(response.content, "lxml")

    post_titles = soup.find_all("a", class_="Link-root Link-isFullCard")

    extracted = []
    for post_title in post_titles:
        extracted.append({
            'title' : post_title.text,
            'link'  : "https://actualidad.rt.com" + post_title['href']
        })

    # Iterate over each post. If the link does not exist in the database, it's new! Add it.
    for post in extracted:
        if db_client.bdd3.rt.find_one({'link': post['link']}) is None:
            # Let's print it out to verify that we added the new post
            print("Found a new listing at the following url: ", post['link'])
            db_client.bdd3.rt.insert(post)
            

