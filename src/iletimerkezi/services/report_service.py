from typing import Optional
from ..http.base import HttpClient
from ..responses.report_response import ReportResponse

class ReportService:
    def __init__(self, http_client: HttpClient, api_key: str, api_hash: str):
        self.http_client = http_client
        self.api_key = api_key
        self.api_hash = api_hash
        self.last_order_id: Optional[int] = None
        self.last_page: Optional[int] = None

    def get(self, order_id: int, page: int = 1) -> ReportResponse:
        """
        Get report for a specific order
        
        Args:
            order_id: The order ID to get report for
            page: Page number for pagination
            row_count: Number of records per page
        """
        self.last_order_id = order_id
        self.last_page = page

        payload = {
            'request': {
                'authentication': {
                    'key': self.api_key,
                    'hash': self.api_hash,
                },
                'order': {
                    'id': order_id,
                    'page': page,
                    'rowCount': 1000,
                },
            },
        }

        response = self.http_client.post('get-report/json', {'json': payload})
        return ReportResponse(response.get_body(), response.get_status_code(), page)

    def next(self) -> ReportResponse:
        """Get the next page of results from the last report request"""
        if not self.last_order_id or not self.last_page:
            raise RuntimeError('No previous report request found. Call get() first.')

        return self.get(self.last_order_id, self.last_page + 1)