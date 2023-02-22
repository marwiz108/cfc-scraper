import requests

URL = "https://www.cfcunderwriting.com"

def main():
    try:
        page = requests.get(URL)
        print(page.text)
    except:
        print("Error getting url")


if __name__ == "__main__":
    main()
