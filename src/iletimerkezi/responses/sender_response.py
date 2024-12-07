from typing import List, Optional
from ..base_response import BaseResponse

class SenderResponse(BaseResponse):
    def __init__(self, response_body: dict, http_status_code: int):
        super().__init__(response_body, http_status_code)
        self._senders: List[str] = []
        self.customize_data()

    def customize_data(self) -> None:
        """Process and store sender data from response"""
        self._senders = self.data.get('senders', {}).get('sender', [])

    def senders(self) -> List[str]:
        """Get list of all sender IDs"""
        return self._senders