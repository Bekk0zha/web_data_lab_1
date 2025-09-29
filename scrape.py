import requests
from bs4 import BeautifulSoup
import csv
import time
from urllib.parse import urljoin

# Set headers to mimic a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Base URL and categories to scrape
base_url = 'http://books.toscrape.com'
categories = [
    'catalogue/category/books/mystery_3/index.html',
    'catalogue/category/books/fiction_10/index.html',
    'catalogue/category/books/nonfiction_13/index.html'
]

# List to store all book data
books_data = []


# Function to scrape a single page
def scrape_page(url):
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all book articles
        books = soup.find_all('article', class_='product_pod')

        for book in books:
            # Extract title
            title = book.find('h3').find('a')['title']

            # Extract price
            price = book.find('p', class_='price_color').text.strip()

            # Extract availability
            availability = book.find('p', class_='instock availability').text.strip()

            # Extract rating
            rating_class = book.find('p', class_='star-rating')['class']
            rating = rating_class[1]  # e.g., 'Three' from ['star-rating', 'Three']

            books_data.append({
                'Title': title,
                'Price': price,
                'Availability': availability,
                'Rating': rating
            })

        # Check for next page
        next_button = soup.find('li', class_='next')
        if next_button:
            next_url = urljoin(url, next_button.find('a')['href'])
            return next_url
        return None
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


# Scrape each category
for category in categories:
    url = urljoin(base_url, category)
    print(f"Scraping category: {url}")

    while url:
        next_url = scrape_page(url)
        url = next_url
        time.sleep(1)  # Respectful delay to avoid overloading the server

# Save to CSV
with open('books_data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['Title', 'Price', 'Availability', 'Rating'])
    writer.writeheader()
    writer.writerows(books_data)

print(f"Saved {len(books_data)} books to books_data.csv")
