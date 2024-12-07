import math
from typing import Dict, List, Optional
from ..base_response import BaseResponse

class ReportResponse(BaseResponse):
    ORDER_STATUS_MESSAGES = {
        113: 'SENDING',
        114: 'COMPLETED',
        115: 'CANCELED'
    }

    MESSAGE_STATUS_MESSAGES = {
        110: 'WAITING',
        111: 'DELIVERED',
        112: 'UNDELIVERED'
    }

    def __init__(self, response_body: Dict, http_status_code: int, current_page: int):
        super().__init__(response_body, http_status_code)
        self._messages: List[Dict] = []
        self._current_page = current_page
        self.customize_data()

    def customize_data(self) -> None:
        self._messages = self.data.get('order', {}).get('message', [])

    def order_id(self) -> str:
        return self.data.get('order', {}).get('id', '')

    def order_status(self) -> str:
        status = self.data.get('order', {}).get('status', '')
        return self.ORDER_STATUS_MESSAGES.get(status, status)

    def order_status_code(self) -> int:
        return int(self.data.get('order', {}).get('status', 0))

    def order_total(self) -> int:
        return int(self.data.get('order', {}).get('total', 0))

    def order_delivered(self) -> int:
        return int(self.data.get('order', {}).get('delivered', 0))

    def order_undelivered(self) -> int:
        return int(self.data.get('order', {}).get('undelivered', 0))

    def order_waiting(self) -> int:
        return int(self.data.get('order', {}).get('waiting', 0))
    
    def order_submit_at(self) -> str:
        return self.data.get('order', {}).get('submitAt', '')

    def order_send_at(self) -> str:
        return self.data.get('order', {}).get('sendAt', '')

    def order_sender(self) -> str:
        return self.data.get('order', {}).get('sender', '')

    def messages(self) -> List[Dict]:
        for message in self._messages:
            status_code = message.get('status')
            message['statusCode'] = status_code
            message['status'] = self.MESSAGE_STATUS_MESSAGES.get(status_code, 'Unknown Status')

        return self._messages

    def total_pages(self) -> int:
        return math.ceil(self.order_total() / 1000)

    def current_page(self) -> int:
        return self._current_page

    def has_more_pages(self) -> bool:
        return self.current_page() < self.total_pages()