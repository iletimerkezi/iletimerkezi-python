from typing import Optional
from ..http.base import HttpClient
from ..responses.summary_response import SummaryResponse

class SummaryService:
    def __init__(self, http_client: HttpClient, api_key: str, api_hash: str):
        """
        Initialize SummaryService
        
        Args:
            http_client: HTTP client instance
            api_key: API key for authentication
            api_hash: API hash for authentication
        """
        self.http_client = http_client
        self.api_key = api_key
        self.api_hash = api_hash
        self.last_start_date: Optional[str] = None
        self.last_end_date: Optional[str] = None
        self.last_page: Optional[int] = None

    def list(self, start_date: str, end_date: str, page: int = 1) -> SummaryResponse:
        """
        Get summary list for date range
        
        Args:
            start_date: Start date in YYYY-MM-DD format
            end_date: End date in YYYY-MM-DD format
            page: Page number for pagination
        """
        self.last_start_date = start_date
        self.last_end_date = end_date
        self.last_page = page

        payload = {
            'request': {
                'authentication': {
                    'key': self.api_key,
                    'hash': self.api_hash,
                },
                'filter': {
                    'start': start_date,
                    'end': end_date,
                },
                'page': page,
            },
        }

        response = self.http_client.post('get-reports/json', {
            'json': payload,
        })

        return SummaryResponse(response.get_body(), response.get_status_code())

    def next(self) -> SummaryResponse:
        """Get the next page of results from the last summary request"""
        if not all([self.last_start_date, self.last_end_date, self.last_page]):
            raise RuntimeError('No previous summary request found. Call list() first.')

        return self.list(self.last_start_date, self.last_end_date, self.last_page + 1)