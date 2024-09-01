from dork_generator import generate_dorks
from search_executor import execute_search
from anonymity_handler import load_proxies_from_file, rotate_proxy, get_proxy_dict
from file_manager import download_files, organize_files
from logger import log_results
from data_filter import filter_recent_data
import time

def main():
    # Load proxies from the local file
    proxies_list = load_proxies_from_file('proxies.txt')

    # Debugging: print loaded proxies
    print(f"Loaded proxies: {proxies_list[:5]}...")  # Show the first few proxies for sanity check

    # Rotate to select one proxy
    proxy = rotate_proxy(proxies_list)
    proxy_dict = get_proxy_dict(proxy)

    # Debugging: print selected proxy
    print(f"Using proxy: {proxy_dict}")

    # Generate dorks
    dorks = generate_dorks("cc")

    for dork in dorks:
        try:
            # Execute search with SOCKS5 proxy, making sure to pass the proxy dict correctly
            soup = execute_search(dork, proxy_dict)
            if soup is None:
                continue
            recent_links = filter_recent_data(soup)

            # Download files
            download_files(recent_links)

            # Log results
            log_results(recent_links)
        except Exception as e:
            print(f"Error occurred during search or download: {e}")  # More debugging output

        # Wait to prevent rate limiting
        time.sleep(10)

    # Organize downloaded files
    organize_files()

if __name__ == "__main__":
    main()
