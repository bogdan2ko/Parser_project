# Parser_project

Parser Project - Otomoto Price Parser for Indian Motorcycles
This project is a Python script that parses the price of Indian motorcycles from the Otomoto website. It utilizes web scraping techniques to extract the relevant information from the website's HTML code and provides the current prices of Indian motorcycles. This README guide will show you how to run the project using Docker and Docker Compose.

## Prerequisites
Before running the project, make sure you have the following installed:

Python 3.x
Celery library (pip install celery)
BeautifulSoup4 library (pip install beautifulsoup4)
Requests library (pip install requests)

## Usage
1. Clone this repository or download the project files to your local machine.

2. Open a terminal or command prompt and navigate to the project directory.

3. Build the Docker image by running the following command:
```
docker-compose build
```
4. Once the build process completes, start the Docker container using the following command:
```
docker-compose up
```
This command will start the container and run the parser script.

5. The script will start parsing the Otomoto website and display the current prices of Indian motorcycles.

## Customization
You can customize the script to parse prices for different motorcycle brands, models, or websites. To do this, follow these steps:

1. Open the tasks.py file in a text editor.

2. Find the URL variable inside the script and update it to the desired website page. For example, to parse prices for a different brand, change the URL accordingly.

3. Adjust the HTML parsing code as per the website's structure and the information you want to extract. You can refer to the BeautifulSoup documentation for more details on how to navigate and extract data from HTML.

4. After making the necessary changes, rebuild the Docker image by running the docker-compose build command again.

5. Finally, start the Docker container with docker-compose up to run the updated script.

##Limitations
Please note the following limitations of the parser:

The script relies on the specific HTML structure of the Otomoto website. If the website structure changes, the parser may not work correctly.

The script only extracts the current prices of Indian motorcycles from the website. It does not provide additional details or perform any analysis.
