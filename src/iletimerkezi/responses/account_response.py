from typing import Dict
from ..base_response import BaseResponse

class AccountResponse(BaseResponse):
    def __init__(self, response_body: Dict, http_status_code: int):
        super().__init__(response_body, http_status_code)
        self._amount: str = '0'
        self._sms: str = '0'
        self.customize_data()

    def customize_data(self) -> None:
        """Process and store balance data from response"""
        balance = self.data.get('balance', {})
        self._amount = balance.get('amount', '0')
        self._sms = balance.get('sms', '0')

    def amount(self) -> str:
        """Get account balance amount"""
        return self._amount

    def credits(self) -> str:
        """Get SMS credits balance"""
        return self._sms