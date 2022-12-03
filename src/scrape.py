import requests
import pandas as pd
import logging
import sys

# Set logging basic to output to sysout
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

class Grabber:

    def __init__(self, use_storage=False):
        self.base_url = "https://www.gutenberg.org/files/100/100-h/100-h.htm"
        self.page_html = "" 
        self.use_storage = use_storage

    '''Uses requests module to grab page data as html, has options for storing data and reading from stored value'''
    def fetch_page(self, write_to_temp=False):
        # TODO : Add some func to specify file name if desired, output to data directory?
        # TODO : If outputting to data directory, include soft fail that makes new dir?
        # Used stored html file
        if self.use_storage == True:
            logging.info("Using stored HTML file!")
            with open('temp.html', "r") as f:
                self.page_html = f.read()
                return
        # Attempt to get the page with requests
        try:
            r = requests.get(self.base_url)
            self.page_html = r.text
            logging.info("Page contents retrieved. Updated page_html") 

        # If the request fails, throw an exception
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)
        # Store data in temp.html if flag is true
        if write_to_temp == True:
            with open("temp.html", "w") as f:
                f.write(self.page_html)
                logging.info("Page html contents written to temp.html file")
                return


# Using main as driver, kinda sloppy. Needs functional test module outside of unit tests
def main():
    gr = Grabber(use_storage=True)
    gr.fetch_page(write_to_temp=True)
    print(gr.page_html[0:100])


if __name__ == "__main__":
    main()
