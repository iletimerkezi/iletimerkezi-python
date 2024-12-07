import json
from typing import Optional, Union, Type, Dict, Any
from .http.base import HttpClient
from .http.urllib_client import UrllibHttpClient
from .services.sms_service import SmsService
from .services.report_service import ReportService
from .services.summary_service import SummaryService
from .services.sender_service import SenderService
from .services.blacklist_service import BlacklistService
from .services.account_service import AccountService
from .services.webhook_service import WebhookService

class IletiMerkeziClient:
    def __init__(
        self, 
        api_key: str, 
        api_hash: str, 
        default_sender: Optional[str] = None,
        http_client: Optional[Union[HttpClient, Type[HttpClient]]] = None
    ):
        """
        Initialize IletiMerkezi client
        
        Args:
            api_key: API key for authentication
            api_hash: API hash for authentication
            default_sender: Optional default sender ID
            http_client: Optional custom HTTP client instance or class
                        Must implement HttpClient interface
        """
        self.api_key = api_key
        self.api_hash = api_hash
        self.default_sender = default_sender
        self.http_client = self._resolve_http_client(http_client)

    def _resolve_http_client(self, client: Optional[Union[HttpClient, Type[HttpClient]]] = None) -> HttpClient:
        """
        Resolve HTTP client instance
        
        Args:
            client: Optional custom HTTP client instance or class
            
        Returns:
            HttpClient instance
        """
        if client is None:
            return UrllibHttpClient()
        if isinstance(client, type):
            return client()
        return client

    def sms(self) -> SmsService:
        return SmsService(self.http_client, self.api_key, self.api_hash, self.default_sender)

    def reports(self) -> ReportService:
        return ReportService(self.http_client, self.api_key, self.api_hash)
    
    def summary(self) -> SummaryService:
        return SummaryService(self.http_client, self.api_key, self.api_hash)

    def senders(self) -> SenderService:
        return SenderService(self.http_client, self.api_key, self.api_hash)

    def blacklist(self) -> BlacklistService:
        return BlacklistService(self.http_client, self.api_key, self.api_hash)

    def account(self) -> AccountService:
        return AccountService(self.http_client, self.api_key, self.api_hash)

    def webhook(self) -> WebhookService:
        return WebhookService()

    def get_http_client(self) -> HttpClient:
        """Get the current HTTP client instance"""
        return self.http_client

    def debug(self) -> str:
        """
        Get debug information about the last request
        
        Returns:
            JSON string containing payload, response and status code
        """
        debug_info: Dict[str, Any] = {
            'payload': json.loads(self.http_client.get_payload()),
            'response': self.http_client.get_body(),
            'status': self.http_client.get_status_code()
        }
        return json.dumps(debug_info, indent=4)