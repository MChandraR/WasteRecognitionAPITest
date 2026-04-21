import requests
from urllib.parse import urljoin
from dotenv import load_dotenv
import os

load_dotenv()

class APITest:
    def __init__(self):
        self.base_url = "http://192.168.1.4:8000/api/"
        self.session = requests.Session()
        self.admin_session = requests.Session()
        self.session.headers.update({
            'User-Agent' : 'Aplikasi/1.0',
            'Accept' : 'application/json',
            'Authorization' : 'Bearer ' + os.getenv("CLIENT_API_TOKEN")
        })

        self.admin_session.headers.update({
            'User-Agent' : 'Aplikasi/1.0',
            'Accept' : 'application/json',
            'Authorization' : 'Bearer ' + os.getenv("ADMIN_API_TOKEN")        })

    def request(self, method, endpoint, payload = None, **kwargs):
        url = urljoin(self.base_url, endpoint)
        
        return self.session.request(method, url, json=payload, **kwargs)
    
    def admin_request(self, method, endpoint, payload = None, **kwargs):
        url = urljoin(self.base_url, endpoint)
        
        # print(f"[LOG] Melakukan {method} ke: {url}") # Debugging prefix
        return self.admin_session.request(method, url, json=payload, **kwargs)

    def test():
        pass 