import requests
from bs4 import BeautifulSoup

def scrape_articles(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the elements that contain the article titles
    article_titles = soup.find_all('h2', class_='article-title')
    
    # Extract the text from the article titles
    titles = [title.text.strip() for title in article_titles]
    
    return titles


if __name__ == '__main__':
    url = 'https://example.com/news'  # Replace with the actual URL
    article_titles = scrape_articles(url)
    for title in article_titles:
        print(title)
