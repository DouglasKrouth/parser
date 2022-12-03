import requests
import pandas as pd

class Grabber:

    def __init__(self):
        self.base_url = "https://www.gutenberg.org/files/100/100-h/100-h.htm"
        
    def fetch_page(self):
        # Attempt to get the page with requests
        try:
            r = requests.get(self.base_url)
            return r.text
        # If the request fails, throw an exception
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)


def main():
    gr = Grabber()
    print(gr[1:100])

if __name__ == "__main__":
    main()
