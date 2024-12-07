from typing import Optional
from ..http.base import HttpClient
from ..responses.blacklist_response import BlacklistResponse
from ..base_response import BaseResponse

class BlacklistService:
    def __init__(self, http_client: HttpClient, api_key: str, api_hash: str):
        """
        Initialize BlacklistService
        
        Args:
            http_client: HTTP client instance
            api_key: API key for authentication
            api_hash: API hash for authentication
        """
        self.http_client = http_client
        self.api_key = api_key
        self.api_hash = api_hash
        self.lastPage = None
        self.lastStart = None
        self.lastEnd = None

    def list(
        self,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        page: int = 1
    ) -> BlacklistResponse:
        """
        Get list of blacklisted numbers
        
        Args:
            start_date: Optional start date in YYYY-MM-DD HH:mm:ss format
            end_date: Optional end date in YYYY-MM-DD HH:mm:ss format
            page: Page number (default: 1)
            row_count: Results per page (default: 1000, max: 1000)
        """

        self.lastStart = start_date
        self.lastEnd = end_date
        self.lastPage = page

        payload = {
            'request': {
                'authentication': {
                    'key': self.api_key,
                    'hash': self.api_hash,
                },
                'blacklist': {
                    'page': page,
                    'rowCount': 1000,
                },
            },
        }

        if start_date and end_date:
            payload['request']['blacklist']['filter'] = {
                'start': start_date,
                'end': end_date,
            }

        response = self.http_client.post('get-blacklist/json', {
            'json': payload,
        })

        return BlacklistResponse(response.get_body(), response.get_status_code(), page)

    def next(self) -> BlacklistResponse:
        """
        Get next page of blacklisted numbers
        
        Args:
            page: Page number (default: 1)
            row_count: Results per page (default: 1000, max: 1000)
        """
        if self.lastPage is None:
            raise Exception("No previous request made")

        return self.list(start_date=self.lastStart, end_date=self.lastEnd, page=self.lastPage + 1)

    def add(self, number: str) -> BaseResponse:
        """
        Add number to blacklist
        
        Args:
            number: Phone number to blacklist
        """
        payload = {
            'request': {
                'authentication': {
                    'key': self.api_key,
                    'hash': self.api_hash,
                },
                'blacklist': {
                    'number': number,
                },
            },
        }

        response = self.http_client.post('add-blacklist/json', {
            'json': payload,
        })

        return BaseResponse(response.get_body(), response.get_status_code())

    def remove(self, number: str) -> BaseResponse:
        """
        Remove number from blacklist
        
        Args:
            number: Phone number to delete from blacklist
        """
        payload = {
            'request': {
                'authentication': {
                    'key': self.api_key,
                    'hash': self.api_hash,
                },
                'blacklist': {
                    'number': number,
                },
            },
        }

        response = self.http_client.post('delete-blacklist/json', {
            'json': payload,
        })

        return BaseResponse(response.get_body(), response.get_status_code())