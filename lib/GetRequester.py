import requests
import json

URL = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        formatted_response = json.loads(self.get_response_body())
        return formatted_response


# request = GetRequester(URL)
