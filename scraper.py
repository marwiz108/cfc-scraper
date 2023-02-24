import requests
from bs4 import BeautifulSoup
import json
import re

HOST = "https://www.cfcunderwriting.com"

def is_external(url):
    # return (tag[attr].startswith("http") or tag[attr].startswith("//")) and "cfcunderwriting" not in tag[attr]
    return (url.startswith("http") or url.startswith("//")) and "cfcunderwriting" not in url

# def has_resource(tag):
#     if (tag.has_attr("href")):
#         return is_external(tag, "href")
#     elif (tag.has_attr("src")):
#         return is_external(tag, "src")
#     else:
#         return False

def get_external_resources(all_urls):
    external_resources = []
    for url in all_urls:
        if is_external(url):
            external_resources.append(url)

    return external_resources

def has_url(tag):
    return tag.has_attr("href") or tag.has_attr("src")

def get_url(tag, attr):
    return tag[attr]

def write_to_file(filename, content):
    with open(filename, "w") as outfile:
        json.dump(content, outfile)
    outfile.close()

def scrape_page(url):
    r = requests.get(url)
    return BeautifulSoup(r.content, "html.parser")

def main():
    index_page = scrape_page(HOST)
    all_resources = index_page.find_all(has_url)  # full tags
    all_urls = [get_url(r, "href") if r.has_attr("href") else get_url(r, "src") for r in all_resources]  # urls

    # json list of external resources
    external_resources = get_external_resources(all_urls)
    write_to_file("external_resources.json", external_resources)

    privacy_page_i = None   # index of privacy policy page
    privacy_url = None      # url of privacy policy page
    for i, url in enumerate(all_urls):
        if "privacy-policy" in url:
            privacy_page_i = i
            privacy_url = url
            break

    print("privacy index: ", privacy_page_i)
    print("privacy url:   ", privacy_url)
    # print(all_resources[privacy_page_i])
    # print(all_urls[privacy_page_i])

    # scrape privacy policy page
    privacy_page = scrape_page(HOST + privacy_url)
    text = privacy_page.get_text(separator=" ", strip=True)
    # with open("privacy_text.txt", "w") as out_f:
    #     out_f.write(text)
    # out_f.close()

if __name__ == "__main__":
    main()
