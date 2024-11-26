import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

book_api_token = os.getenv('book_api_token')


def fetch_book_categories(book_api_token):
    url = f'https://api.nytimes.com/svc/books/v3/lists/names.json?api-key={book_api_token}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        categories = response.json().get('results', [])
        print(f"Total Categories: {len(categories)}")
        return categories
    except requests.RequestException as e:
        print(f"Error fetching book categories: {e}")
        return []


fetch_book_categories(book_api_token)


def retrieve_book_critique(book_api_token, book_isbn, book_title, book_author):
    url = f'https://api.nytimes.com/svc/books/v3/reviews.json?isbn={book_isbn}&title={book_title}&author={book_author}&api-key={book_api_token}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        reviews = response.json().get('results', [])
        print(f"Total Reviews Found: {len(reviews)}")
        return reviews
    except requests.RequestException as e:
        print(f"Error retrieving book review: {e}")
        return []


retrieve_book_critique(book_api_token, '0316066524', 'CURIOUS TIDES', 'Pascale Lacelle')


def explore_bestsellers_timeline(book_api_token, selected_date):
    url = f'https://api.nytimes.com/svc/books/v3/lists/{selected_date}/hardcover-fiction.json?api-key={book_api_token}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        response_data = response.json()

        if response_data.get('num_results', 0) == 0:
            print(f"No bestsellers found for date: {selected_date}")
            return []
        bestsellers = response_data.get('results', [])

        print(f"Bestsellers on {selected_date}: {len(bestsellers)}")
        return bestsellers
    except requests.RequestException as e:
        print(f"Error exploring bestsellers: {e}")
        return []



explore_bestsellers_timeline(book_api_token, '2024-01-21')



def analyze_publication_overview(book_api_token, publication_date):
    url = f'https://api.nytimes.com/svc/books/v3/lists/full-overview.json?published_date={publication_date}&api-key={book_api_token}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        overview = response.json().get('results', {})
        print(f"Publication Overview Date: {publication_date}")
        return overview
    except requests.RequestException as e:
        print(f"Error analyzing publication overview: {e}")
        return {}


analyze_publication_overview(book_api_token, '2024-11-02')


def gather_book_catalog(book_api_token, catalog_date):
    url = f'https://api.nytimes.com/svc/books/v3/lists/overview.json?published_date={catalog_date}&api-key={book_api_token}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        book_catalog = response.json().get('results', {})
        print(f"Book Catalog for {catalog_date} retrieved")
        return book_catalog
    except requests.RequestException as e:
        print(f"Error gathering book catalog: {e}")
        return {}


gather_book_catalog(book_api_token, '2024-11-22')


def track_bestseller_rankings(book_api_token):
    url = f'https://api.nytimes.com/svc/books/v3/lists.json?list=hardcover-fiction&bestsellers-date=3596-14-26&published-date=3596-14-26&offset=20&api-key={book_api_token}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        rankings = response.json().get('results', [])
        print(f"Bestseller Rankings Retrieved: {len(rankings)}")
        return rankings
    except requests.RequestException as e:
        print(f"Error tracking bestseller rankings: {e}")
        return []


track_bestseller_rankings(book_api_token)


def discover_top_publications(book_api_token):
    url = f'https://api.nytimes.com/svc/books/v3/lists/best-sellers/history.json?age-group=14&author=Michael Connelly&contributor=iraguha&isbn=0316066524&offset=20&price=2345&publisher=alexis&title=Great signs&api-key={book_api_token}'

    try:
        response = requests.get(url)
        response.raise_for_status()
        top_publications = response.json().get('results', [])
        print(f"Top Publications Discovered: {len(top_publications)}")
        return top_publications
    except requests.RequestException as e:
        print(f"Error discovering top publications: {e}")
        return []


discover_top_publications(book_api_token)