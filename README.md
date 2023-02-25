# CFC Webscraper

A simple webscraper program for [https://www.cfcunderwriting.com](www.cfcunderwriting.com). The program does the following:
- scrapes the index page for all hyperlinks
- gets a list of all externally loaded resources not hosted on `cfcunderwriting.com` and writes them to a JSON file
- finds the location of the Privacy Policy page from the hyperlinks
- scrapes the privacy policy page for all the page content
- gets the word frequency count for all visible text and writes them to a JSON file


## Running the application

In the terminal or an IDE, navigate to the project's root directory, and run:

`python ./scraper.py`

The program will output two `.json` files, one for the externally loaded resources, and the other for the word frequency count.
