from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):

    def do_GET(self):

        path = self.path
        url_components = parse.urlsplit(path)
        query_string_list = parse.parse_qsl(url_components.query)
        print(query_string_list)
        dictionary = dict(query_string_list)
        url = "https://restcountries.com/v3.1/"
        country = dictionary.get("country")
        capital = dictionary.get("capital")

        if capital:
            response = requests.get(url + "capital/" + capital)
            data = response.json()
            capitals = data[0]["capital"]
            country_name = data[0]["name"]["common"]
             
            message = f"The capital of {country_name} is {capitals[0]}"

        elif country:
            response = requests.get(url + "name/" + country)
            data = response.json()
            capital_response = data[0]["capital"]

            message = f"{capital_response[0]} is the capital of {country}"

        else:
            message = "Give me a valid country please"

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(message.encode())
        return