
import requests
from celery import shared_task
from bs4 import BeautifulSoup

@shared_task
def parse_otomoto_prices(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        raise Exception(f"Failed to retrieve data from otomoto API. Error: {str(e)}")

    try:
        prices = []
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Извлекаем элемент титула
        title_element = soup.select_one('h2[data-testid="ad-title"]')
        if title_element:
            title = title_element.text.strip()
        else:
            title = None
        
        # Извлекаем цены
        price_elements = soup.select('span.ooa-1bmnxg7.evg565y13')
        prices = [element.text.strip() for element in price_elements]

        return title, prices
    except Exception as e:
        raise Exception(f"Failed to parse otomoto data. Error: {str(e)}")