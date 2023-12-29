import requests
from bs4 import BeautifulSoup

class CategoryTaxonomy():

    def __init__(self):
        self.url = "https://arxiv.org/category_taxonomy"
        self.tag_map = self.get_tag_map()        

    def get_tag_map(self):
        headers = self.get_h4_headers(self.url)

        tag_map = {}
        for header in headers:
            tag, human_readable = self.split_header(header)
            if tag == 'Category Name':
                continue
            else:
                tag_map[tag] = human_readable
        self.tag_map = tag_map
        return tag_map

    def get_h4_headers(self, url):
        """
        Fetch the HTML content of a website and return all H4 headers.

        Parameters:
        - url (str): The URL of the website.

        Returns:
        - list: A list of H4 headers found on the webpage.
        """
        try:
            # Fetch the HTML content
            response = requests.get(url)
            response.raise_for_status()

            # Parse the HTML content with BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all H4 headers
            h4_headers = [h4.text for h4 in soup.find_all('h4')]
            return h4_headers
        except Exception as e:
            print(f"Error: {e}")
            return None

    def split_header(self, header):
        """
        Split a header into its category and subcategory.

        Parameters:
        - header (str): The header to be split.

        Returns:
        - tuple: A tuple containing the category and subcategory.
        """
        try:
            category, subcategory = header.replace(')','').split('(')
            return (category.strip(), subcategory.strip())
        except Exception as e:
            print(f"Error: {e}")
            return None
    

# t = CategoryTaxonomy()
# t.get_tag_map()
# print(t.tag_map)