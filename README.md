# CFC Webscraper

A simple webscraper program for [www.cfcunderwriting.com](https://www.cfcunderwriting.com). The program does the following:
- scrapes the index page for all hyperlinks
- gets a list of all externally loaded resources not hosted on `cfcunderwriting.com` and writes them to a JSON file
- finds the location of the Privacy Policy page from the hyperlinks
- scrapes the privacy policy page for all the page content
- gets the word frequency count for all visible text and writes them to a JSON file


## Running the application

In the terminal or an IDE, navigate to the project's root directory, and run:

`pip install -r requirements.txt`

`python ./scraper.py`

Note: make sure you are using pip and python versions > 3.

The program will output two `.json` files, one for the externally loaded resources, and the other for the word frequency count.
