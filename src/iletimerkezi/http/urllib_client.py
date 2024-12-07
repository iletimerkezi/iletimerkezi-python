from typing import Dict, Any
import json
import urllib.request
import urllib.error
import urllib.parse
from .base import HttpClient

class UrllibHttpClient(HttpClient):
    BASE_URL = 'https://api.iletimerkezi.com/v1/'
    
    def __init__(self):
        self.body = {}
        self.status_code = 0
        self.payload = ''
        
    def post(self, url: str, options: Dict[str, Any]) -> 'HttpClient':
        full_url = self.BASE_URL + url
        self.payload = json.dumps(options.get('json', {}))
        
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
        
        try:
            request = urllib.request.Request(
                full_url,
                data=self.payload.encode('utf-8'),
                headers=headers,
                method='POST'
            )
            
            with urllib.request.urlopen(request) as response:
                self.status_code = response.status
                self.body = json.loads(response.read().decode('utf-8'))
                
        except urllib.error.URLError as e:
            if hasattr(e, 'code'):
                self.status_code = e.code
            if hasattr(e, 'read'):
                self.body = json.loads(e.read().decode('utf-8'))
            else:
                self.body = {'error': str(e)}
                
        return self
        
    def get_body(self) -> Dict[str, Any]:
        return self.body
        
    def get_status_code(self) -> int:
        return self.status_code
        
    def get_payload(self) -> str:
        return self.payload