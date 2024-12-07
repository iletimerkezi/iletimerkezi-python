import math
from typing import Dict, List, Optional
from ..models.summary import Summary
from ..base_response import BaseResponse

class SummaryResponse(BaseResponse):
    def __init__(self, response_body: Dict, http_status_code: int, page: int = 1):
        super().__init__(response_body, http_status_code)
        self._orders: List[Dict] = []
        self.customize_data()
        self._current_page = page

    def customize_data(self) -> None:
        """Process and store orders data from response"""
        self._orders = self.data.get('orders', {})

    def get_count(self) -> int:
        """Get total order count"""
        return self.data.get('count', 0)

    def get_orders(self) -> List[Summary]:
        """Get all orders"""
        return [Summary(order) for order in self._orders]

    def get_total_pages(self) -> int:
        """Get total page count"""
        return math.ceil(self.get_count() / 30)

    def get_current_page(self) -> int:
        """Get current page number"""
        return self._current_page

    def has_more_pages(self) -> bool:
        """Check if there are more pages"""
        return self.get_current_page() < self.get_total_pages()