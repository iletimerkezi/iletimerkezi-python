from typing import Union, List, Dict, Optional
from ..http.base import HttpClient
from ..responses.sms_response import SmsResponse

class SmsService:
    def __init__(
        self, 
        http_client: HttpClient, 
        api_key: str, 
        api_hash: str, 
        default_sender: Optional[str] = None
    ):
        self.http_client = http_client
        self.api_key = api_key
        self.api_hash = api_hash
        self.default_sender = default_sender
        self.send_date_time = ''
        self.iys = '1'
        self.iys_list = 'BIREYSEL'

    def schedule(self, send_date_time: str) -> 'SmsService':
        """Set the sendDateTime for scheduling messages."""
        self.send_date_time = send_date_time
        return self

    def enable_iys_consent(self) -> 'SmsService':
        """Enable IYS consent flag."""
        self.iys = '1'
        return self

    def disable_iys_consent(self) -> 'SmsService':
        """Disable IYS consent flag."""
        self.iys = '0'
        return self

    def iys_list_type(self, iys_list: str) -> 'SmsService':
        """Set the IYS list type (e.g., BIREYSEL or TACIR)."""
        self.iys_list = iys_list
        return self

    def send(
        self, 
        recipients: Union[str, List[str], Dict[str, str]], 
        message: Optional[str] = None, 
        sender: Optional[str] = None
    ) -> SmsResponse:
        """
        Send SMS message(s)
        
        Args:
            recipients: Can be:
                - A single phone number (str)
                - List of phone numbers (List[str])
                - Dict of phone numbers to messages (Dict[str, str])
            message: The message text (required if recipients is str or List[str])
            sender: Optional sender ID (falls back to default_sender)
        """
        payload = {
            'request': {
                'authentication': {
                    'key': self.api_key,
                    'hash': self.api_hash,
                },
                'order': {
                    'sender': sender or self.default_sender,
                    'sendDateTime': self.send_date_time,
                    'iys': self.iys,
                    'iysList': self.iys_list,
                    'message': self._build_messages(recipients, message),
                },
            },
        }

        response = self.http_client.post('send-sms/json', {'json': payload})
        return SmsResponse(response.get_body(), response.get_status_code())

    def _build_messages(
        self, 
        recipients: Union[str, List[str], Dict[str, str]], 
        message: Optional[str]
    ) -> Dict:
        """Build the message payload based on the type of recipients."""
        if isinstance(recipients, str):
            return {
                'text': message,
                'receipents': {
                    'number': [recipients]
                }
            }
        
        if isinstance(recipients, list):
            if message is None:
                raise ValueError("Message is required when recipients is a list")
            return {
                'text': message,
                'receipents': {
                    'number': recipients
                }
            }
        
        if isinstance(recipients, dict):
            messages = []
            for number, text in recipients.items():
                messages.append({
                    'text': text,
                    'receipents': {
                        'number': [number]
                    }
                })
            return messages
        
        raise ValueError('Invalid recipients format')