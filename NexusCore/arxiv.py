import urllib, urllib.request
import requests
from bs4 import BeautifulSoup
import xmltodict
import json
from category_taxonomy import CategoryTaxonomy
import re

class ArxivDigest():

    def __init__(self) -> None:
        ct = CategoryTaxonomy()
        self.db_loc = "database.json"
        self.db = self.load_db()
        self.tag_map = ct.get_tag_map()
        self.api_url = "http://export.arxiv.org/api/"

    def init_all_papers(self):
        for category in self.tag_map.keys():
            self.get_recent_papers(category)
        return
    
    def get_recent_papers(self, category):
        id_list = self.get_most_recent_ids(category)
        id_string = ""
        for item in id_list:
            id_string += f"{item},"
        res = self.query_arxiv(f"cat:{category}&id_list={id_string}", len(id_list))
        res = self.extract_key_fields_from_query_response(res)
        for paper in res:
            print(paper)
            category = paper['primary_category']["@term"]
            self.db[category][paper['title']] = paper
        self.save_db()
        return res

    def load_db(self):
        with open(self.db_loc, 'r') as f:
            return json.load(f)

    def save_db(self):
        with open(self.db_loc, 'w') as f:
            json.dump(self.db, f, indent=2)

    def init_db(self):
        # WILL OVERWRITE EXISTING DB
        if self.db == {}:
            for i in self.tag_map:
                self.db[i] = {}
        with open(self.db_loc, 'w') as f:
            json.dump(self.db, f, indent=2)
        self.save_db()

    def convert_xml_to_json(self, xml_data):
        """
        Convert XML data to JSON.

        Parameters:
        - xml_data (str): The XML data to be converted.

        Returns:
        - str: The JSON representation of the XML data.
        """
        try:
            # Parse XML to OrderedDict
            xml_dict = xmltodict.parse(xml_data)
            # Convert OrderedDict to JSON
            # json_data = json.dumps(xml_dict, indent=2)
            return xml_dict
        except Exception as e:
            print(f"Error converting XML to JSON: {e}")
            return None

    def query_arxiv(self, search_query, max_results=10):
        """
        Query arXiv for papers matching the given search query.

        Parameters:
        - search_query (str): The search query.
        - max_results (int): The maximum number of results to return.

        Returns:
        - str: The JSON representation of the search results.
        """
        try:
            # Construct the URL for the query
            url = f"{self.api_url}query?search_query={search_query}&max_results={max_results}"
            # Fetch the XML data
            data = urllib.request.urlopen(url)
            xml_data = data.read().decode('utf-8')
            # Convert XML to JSON
            json_data = self.convert_xml_to_json(xml_data)
            return json_data
        except Exception as e:
            print(f"Error querying arXiv: {e}")
            return None

    def get_most_recent_ids(self, category):
        # Fetch the HTML content
        response = requests.get(f"https://arxiv.org/list/{category}/recent")
        response.raise_for_status()

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all H4 headers
        dt_tags = [dt.text for dt in soup.find_all('dt')]
        pattern = r'arXiv:\d{4}\.\d+'

        matches = re.findall(pattern, str(dt_tags))

        id_list = []
        for match in matches:
            try:
                id = match.split(':')[1]
                id_list.append(id)
            except:
                continue
        return id_list

    def extract_key_fields_from_query_response(self, query_response):
        entries = query_response["feed"]["entry"]

        if not isinstance(entries, list):
            entries = [entries]

        object_results = []
        for entry in entries:
            try:
                # categories = self.build_categories(entry["category"])
                # authors = map(lambda x: x["name"], entry["author"])
                # print(entry["author"])
                if type(entry["author"]) == dict:
                    authors = entry["author"]["name"]
                else:
                    authors = [person['name'] for person in entry['author']]
                    authors = ', '.join(authors)
                # print(authors)
                res = {
                    "url": entry["id"],
                    "id": entry["id"].split('/')[-1],
                    "html_link": f"https://browse.arxiv.org/html/{entry['id'].split('/')[-1]}",
                    "links": entry["link"],
                    "categories": entry["category"],
                    "primary_category": entry["arxiv:primary_category"],
                    "title": entry["title"].replace('\n', '').replace('  ', ' '),
                    "summary": entry["summary"].replace('\n', ' '),
                    "published": entry["published"],
                    "authors": authors,
                    "authors_object": entry["author"]
                }
                object_results.append(res)
            except Exception as e:
                print(f"Error extracting key fields from query response: {e}")
                continue
        return object_results

    def build_categories(self, categories):
        if not isinstance(categories, list):
            categories = [categories]
        category_list = []
        for category in categories:
            category_list.append(self.tag_map[category["@term"]])
        return category_list

        

a = ArxivDigest()
# res = a.query_arxiv("all:cs.CV&max_results=3")
# res = a.extract_key_fields_from_query_response(res)
a.init_db()
# a.get_recent_papers("cs.CV")
a.init_all_papers()

