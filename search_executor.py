import requests
from bs4 import BeautifulSoup

def execute_search(dork, proxies):
    headers = {'User-Agent': 'Mozilla/5.0'}
    search_url = f"https://www.google.com/search?q={dork}"

    print(f"Searching with URL: {search_url} and proxies: {proxies}")  # Debugging output

    try:
        response = requests.get(search_url, headers=headers, proxies=proxies, timeout=10)
        response.raise_for_status()  # Raise an error if the request fails
        soup = BeautifulSoup(response.text, 'lxml')
        return soup
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
