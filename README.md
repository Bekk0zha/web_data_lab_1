Web Scraping Report

Website Structure Analysis

The target website, books.toscrape.com, is a mock e-commerce platform designed for scraping practice. Its structure is consistent across category pages, with books listed in <article class="product_pod"> elements. Each book contains:





Title: Nested in an <h3> tag, within an <a> tag’s title attribute.



Price: Contained in a <p class="price_color"> element.



Availability: Found in a <p class="instock availability"> element.



Rating: Indicated by a <p class="star-rating"> element with a class like star-rating Three.

Category pages include pagination links in a <li class="next"> element, allowing navigation to subsequent pages. The site’s robots.txt permits scraping, as it is intended for educational purposes.

Main Challenges in Scraping





Pagination Handling: Category pages may span multiple pages, requiring dynamic navigation to collect all data.



Rate Limiting: Frequent requests could overwhelm the server or trigger blocks, necessitating respectful scraping practices.



Data Consistency: Ensuring extracted data (e.g., ratings) is correctly interpreted, as ratings are stored as class names (e.g., “Three” for 3 stars).



Error Handling: Network issues or changes in page structure could disrupt scraping.

Solutions Implemented





Pagination: The script checks for a “next” button and constructs the next page’s URL using urljoin to handle relative paths, looping until no further pages exist.



Rate Limiting: A 1-second delay between requests (time.sleep(1)) ensures respectful scraping.



Data Extraction: BeautifulSoup’s CSS selector methods reliably extract fields. Ratings are derived from the second class name of the star-rating element.



Error Handling: The script uses try-except to catch HTTP errors and skips problematic pages, ensuring robustness.



Output: Data is stored in a CSV file using the csv module, ensuring structured and accessible output.

The script successfully scrapes three categories (Mystery, Fiction, Nonfiction), extracting title, price, availability, and rating, and saves the data in books_data.csv.
