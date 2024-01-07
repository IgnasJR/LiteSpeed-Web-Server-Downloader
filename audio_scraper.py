import requests
from bs4 import BeautifulSoup
import urllib.request
import os
import sys
from urllib.parse import urljoin

def DownloadFilesFromUrl(url, download_folder):
    base_url = 'https://mp3.hardcore.lt/'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            file_links = soup.find_all('a', href=True)

            if not os.path.exists(download_folder):
                os.makedirs(download_folder)

            for link in file_links:
                file_url = link['href']
                if file_url.endswith(('.mp3', '.ogg', '.waw', '.flac')):
                    absolute_file_url = urljoin(base_url, file_url)
                    filename = os.path.basename(absolute_file_url)
                    file_path = os.path.join(download_folder, filename)
                    try:
                        urllib.request.urlretrieve(absolute_file_url, file_path)
                        print(f"Downloaded: {filename}")
                    except Exception as e:
                        print(f"Failed to download {filename}: {e}")
        else:
            print(f"Failed to fetch HTML. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Failed to fetch HTML: {e}")

if len(sys.argv) > 1:
    custom_url = sys.argv[1]
    download_folder = sys.argv[2] if len(sys.argv) > 2 else "downloads"
    DownloadFilesFromUrl(custom_url, download_folder)
else:
    print("Please provide a URL.")
