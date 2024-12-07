from ..http.base import HttpClient
from ..responses.account_response import AccountResponse

class AccountService:
    def __init__(self, http_client: HttpClient, api_key: str, api_hash: str):
        """
        Initialize AccountService
        
        Args:
            http_client: HTTP client instance
            api_key: API key for authentication
            api_hash: API hash for authentication
        """
        self.http_client = http_client
        self.api_key = api_key
        self.api_hash = api_hash

    def balance(self) -> AccountResponse:
        """
        Get account balance information
        
        Returns:
            AccountResponse containing balance details
        """
        payload = {
            'request': {
                'authentication': {
                    'key': self.api_key,
                    'hash': self.api_hash
                }
            }
        }

        response = self.http_client.post('get-balance/json', {
            'json': payload,
        })

        return AccountResponse(response.get_body(), response.get_status_code())