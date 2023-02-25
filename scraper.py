import requests
from bs4 import BeautifulSoup
import json
import re
import collections

HOST = "https://www.cfcunderwriting.com"

def get_privacy_policy_location(all_urls):
    for _, url in enumerate(all_urls):
        if "privacy-policy" in url:
            return url

def get_external_resources(all_urls):
    external_resources = []
    for url in all_urls:
        if is_external(url):
            external_resources.append(url)

    return external_resources

def is_external(url):
    return (url.startswith("http") or url.startswith("//")) and "cfcunderwriting" not in url

def get_url(tag, attr):
    return tag[attr]

def has_url(tag):
    return tag.has_attr("href") or tag.has_attr("src")

def write_to_json_file(filename, content):
    with open(filename, "w") as outfile:
        json.dump(content, outfile)
    outfile.close()

def scrape_page(url):
    r = requests.get(url)
    return BeautifulSoup(r.content, "html.parser")

def main():
    # scrape index page
    index_page = scrape_page(HOST)
    all_resources = index_page.find_all(has_url)  # full tags
    all_urls = [get_url(r, "href") if r.has_attr("href") else get_url(r, "src") for r in all_resources]  # urls

    # list of external resources
    external_resources = get_external_resources(all_urls)
    write_to_json_file("external_resources.json", external_resources)

    privacy_page_location = get_privacy_policy_location(all_urls)

    # scrape privacy policy page
    privacy_page = scrape_page(HOST + privacy_page_location)
    text = privacy_page.get_text(separator=" ", strip=True)
    # use regex to strip the text of special characters and numbers
    stripped_text = re.sub("[^a-zA-Z\s]", "", text)
    text_list = stripped_text.lower().split()
    # create a Counter object to calculate word frequencies
    frequencies = collections.Counter(text_list)
    write_to_json_file("word_count.json", dict(frequencies))

if __name__ == "__main__":
    main()
