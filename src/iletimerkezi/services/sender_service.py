from ..http.base import HttpClient
from ..responses.sender_response import SenderResponse

class SenderService:
    def __init__(self, http_client: HttpClient, api_key: str, api_hash: str):
        """
        Initialize SenderService
        
        Args:
            http_client: HTTP client instance
            api_key: API key for authentication
            api_hash: API hash for authentication
        """
        self.http_client = http_client
        self.api_key = api_key
        self.api_hash = api_hash

    def list(self) -> SenderResponse:
        """
        Get list of approved sender IDs
        
        Returns:
            SenderResponse containing list of sender IDs
        """
        payload = {
            'request': {
                'authentication': {
                    'key': self.api_key,
                    'hash': self.api_hash,
                },
            },
        }

        response = self.http_client.post('get-sender/json', {
            'json': payload,
        })

        return SenderResponse(response.get_body(), response.get_status_code())