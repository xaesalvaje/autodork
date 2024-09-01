import requests
import random
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

def load_proxies_from_file(proxy_file_path):
    with open(proxy_file_path, 'r') as file:
        proxies = file.readlines()
    return [proxy.strip() for proxy in proxies if proxy.strip() and ":" in proxy]  # Filter out invalid linesimport random

def load_proxies_from_file(proxy_file_path):
    with open(proxy_file_path, 'r') as file:
        proxies = file.readlines()
    return [proxy.strip() for proxy in proxies if proxy.strip() and ":" in proxy]  # Filter out invalid lines

def rotate_proxy(proxies):
    return random.choice(proxies)

def get_proxy_dict(proxy):
    return {
        'http': f'socks5://{proxy}',
        'https': f'socks5://{proxy}',
    }
