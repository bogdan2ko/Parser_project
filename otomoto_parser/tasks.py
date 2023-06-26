import requests
from celery import shared_task

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
        start_marker = '<span class="ooa-1bmnxg7 evg565y13">'
        end_marker = '</span>'
        start_index = html_content.find(start_marker)

        while start_index != -1:
            end_index = html_content.find(end_marker, start_index)
            price = html_content[start_index + len(start_marker):end_index].strip()
            prices.append(price)
            start_index = html_content.find(start_marker, end_index)

        return prices
    except Exception as e:
        raise Exception(f"Failed to parse otomoto prices. Error: {str(e)}")

