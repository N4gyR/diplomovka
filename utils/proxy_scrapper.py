import requests
from bs4 import BeautifulSoup
from utils.logger import Logger

logger = Logger(name="proxy_scrapper").logger
# Get free proxies for rotating
def get_free_proxies():
    logger.info("Scrapping proxy")
    url = 'https://sslproxies.org'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table')
    thead = table.find('thead').find_all('th')
    tbody = table.find('tbody').find_all('tr', limit=6)  # Only get 6 rows

    headers = [th.text.strip() for th in thead]

    proxies = []
    for tr in tbody:
        proxy_data = {}
        tds = tr.find_all('td')
        for i in range(len(headers)):
            proxy_data[headers[i]] = tds[i].text.strip()
        proxies.append(proxy_data)
    logger.info("Proxy scrapped successfull")
    return proxies[0]["IP Address"], proxies[0]["Port"]


