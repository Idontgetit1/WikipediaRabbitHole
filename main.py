#import requests
import json
import wikipedia
import random

#get random wikipedia page return wikipedia page
def get_random_wikipedia_page():
    wikipedia.set_lang("en")
    page = wikipedia.page(wikipedia.random())

    return page

#get all links on wikipedia page
def get_links_on_page(page):
    links = wikipedia.page(page).links
    return links

def main(depth):
    start_page = get_random_wikipedia_page()

    print("start: " + start_page.title)
    print(start_page.url)

    path = []
    path.append(start_page)

    current_page = start_page

    for i in range(depth):
        #get links on page
        links = get_links_on_page(current_page)

        #get random link
        random_link = random.choice(links)

        #get page
        page = wikipedia.page(random_link)

        #add page to path
        path.append(page)

        #set current page to page
        current_page = page

    #print path nice
    for page in path:
        print(page.title)
        print(page.url)

main(5)