import requests

def test_proxy(proxy):
    proxy_dict = {
        'http': f'socks5://{proxy}',
        'https': f'socks5://{proxy}',
    }
    test_url = "https://www.google.com"
    try:
        response = requests.get(test_url, proxies=proxy_dict, timeout=10)
        if response.status_code == 200:
            print(f"Proxy {proxy} is working.")
            return True
        else:
            print(f"Proxy {proxy} failed with status code {response.status_code}.")
    except requests.exceptions.RequestException as e:
        print(f"Proxy {proxy} failed: {e}")
    return False

def load_proxies_from_file(proxy_file_path):
    with open(proxy_file_path, 'r') as file:
        proxies = file.readlines()
    return [proxy.strip() for proxy in proxies if proxy.strip() and ":" in proxy]

def main():
    proxies_list = load_proxies_from_file('proxies.txt')

    working_proxies = []
    for proxy in proxies_list:
        if test_proxy(proxy):
            working_proxies.append(proxy)

    print(f"Working proxies: {working_proxies}")

if __name__ == "__main__":
    main()
